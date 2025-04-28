
import os
import csv
import json
import re
import glob
import openai
import pandas as pd
import matplotlib.pyplot as plt

# KONFIGURACE
QUERY_CSV_PATH = "nl_queries_selected.csv"         # CSV s id, prompty, db_folder
BASE_DATA_FOLDER = "databases_cze"         # základní složka s podsložkami (pojmenované podle db_folder)
OUTPUT_RESPONSES = "responses_cze"
OUTPUT_GRAPHS = "graphs_cze"
MODEL = "gpt-4o-mini"
TEMPERATURE = 0.7

os.makedirs(OUTPUT_RESPONSES, exist_ok=True)
os.makedirs(OUTPUT_GRAPHS, exist_ok=True)

client = openai.OpenAI()

def extract_and_run_code(response_text: str, output_path: str) -> str:
    match = re.search(r"```python(.*?)```", response_text, re.DOTALL)
    if not match:
        return "❌ Žádný kód nenalezen"
    code = match.group(1).strip()

    # Odstraníme případné plt.show(), které brání uložení
    code = re.sub(r"plt\.show\(\)", "", code)

    try:
        local_env = {}
        exec(code, {"plt": plt, "pd": pd}, local_env)

        fig_nums = plt.get_fignums()
        if not fig_nums:
            return "❌ Kód nevytvořil žádný graf"

        fig = plt.figure(fig_nums[-1])
        fig.savefig(output_path)
        plt.close('all')
        return "✅ Graf uložen"
    except Exception as e:
        return f"❌ Chyba při vykreslení: {e}"


def load_csvs_from_folder(folder_path: str) -> str:
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    contents = []
    for file_path in csv_files:
        try:
            df = pd.read_csv(file_path)
            contents.append(f"Soubor: {os.path.basename(file_path)}\n" + df.to_csv(index=False))
        except Exception as e:
            contents.append(f"❌ Chyba při čtení {file_path}: {e}")
    return "\n\n".join(contents)

def run_pipeline(prompt_type: str = "cze_queries"):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    with open(QUERY_CSV_PATH, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        queries = [row for row in reader]

    results = []

    for row in queries:
        query_id = row["id"]
        db_folder = row.get("db_folder", "").strip()
        prompts = [p.strip() for p in row.get(prompt_type, "").split("|") if p.strip()]
        if not prompts or not db_folder:
            continue

        folder_path = os.path.join(BASE_DATA_FOLDER, db_folder)
        if not os.path.isdir(folder_path):
            context_data = "❌ Složka s daty nenalezena."
        else:
            context_data = load_csvs_from_folder(folder_path)

        for i, prompt in enumerate(prompts, 1):
            full_id = f"{query_id}_{i}"

            system_prompt = f"""Jsi odborník na vizualizaci dat.
Níže jsou data, která máš použít k zodpovězení dotazu. Vygeneruj odpověď včetně generování grafu v Python kódu (např. matplotlib nebo pandas pro graf). Do python kódu nezahrnuj žádné další části workflow. Data potřebná pro generování grafu zjisti na začátku a vypiš je do Python kódu ne jako odkaz na csv, ale jako čísla a názvy proměnných:

{context_data}
"""

            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    temperature=TEMPERATURE,
                    max_tokens=700,
                    top_p=1,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ]
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"❌ Chyba při volání modelu: {e}"

            response_path = os.path.join(OUTPUT_RESPONSES, f"{full_id}_{prompt_type}.txt")
            with open(response_path, "w", encoding="utf-8") as f:
                f.write(reply)

            graph_path = os.path.join(OUTPUT_GRAPHS, f"{full_id}_{prompt_type}.png")
            status = extract_and_run_code(reply, graph_path)

            results.append({
                "id": full_id,
                "prompt_type": prompt_type,
                "prompt": prompt,
                "response_file": response_path,
                "graph_file": graph_path if "✅" in status else "",
                "code_status": status
            })

    summary_path = f"results_summary_{prompt_type}.csv"
    with open(summary_path, "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["id", "prompt_type", "prompt", "response_file", "graph_file", "code_status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"✅ Hotovo. Výstup uložen do {summary_path}")
