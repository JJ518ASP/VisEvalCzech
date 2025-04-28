# VisEvalCzech
## Struktura a popis hlavních podsložek a souborů repozitáře VisEvalCzech

Repozitář **VisEvalCzech** obsahuje českou lokalizaci benchmarku VisEval pro hodnocení schopností LLMs generovat vizualizace na základě přirozeného jazyka. Níže je popsána struktura hlavních složek a klíčových souborů, s důrazem na jejich funkci.

---

## Hlavní složky a soubory

# Struktura a popis hlavních složek a souborů repozitáře VisEvalCzech

| Název                          | Popis                                                                                                                                                                                                                                    |
|------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `databases/`                   | Obsahuje data a schémata databází, která slouží jako zdroj pro vizualizační dotazy v benchmarku. Každá podsložka reprezentuje jednu databázi s ukázkovými tabulkami a daty pro generování a ověřování vizualizací.                        |
| `graphs/`                      | Složka pro ukládání vizualizačních výstupů, například vygenerovaných grafů ve formátu obrázků nebo JSON specifikací. Umožňuje porovnávat výstupy různých modelů či experimentů.                                                         |
| `responses/`                   | Obsahuje odpovědi modelů na jednotlivé dotazy benchmarku. Najdete zde výstupy LLMs v různých jazykových verzích i případné referenční odpovědi pro evaluaci přesnosti a interpretovatelnosti generovaných vizualizací.                   |
| `README.md`                    | Hlavní dokumentace repozitáře. Stručně popisuje účel projektu, jeho strukturu a základní instrukce pro použití. Obsahuje také informace o původu dat a odkazy na metodologii lokalizace.                                               |
| `LICENSE`                      | Licenční podmínky projektu (MIT License), které umožňují volné použití a úpravy dat.                                                                                                             |
| `validace.xlsx`                | Obsahuje podrobné porovnání výsledků experimentu. Slouží k dokumentaci a analýze přesnosti, interpretovatelnosti a dalších kvalitativních parametrů vygenerovaných vizualizací v jednotlivých jazykových verzích.                       |
| `run.py`                       | Jednoduchý spouštěcí skript pro inicializaci a řízení běhu hlavního experimentu. Volá hlavní funkci a nastavuje základní parametry běhu.                                                                                               |
| `generate_from_queries_final.py`| Hlavní skript projektu, ve kterém jsou definovány specifikace a konfigurace použitého jazykového modelu. Obsahuje kompletní logiku pro generování vizualizačních výstupů, zpracování promptů a manipulaci s vygenerovanými hodnotami. |
| `nl_queries_selected.csv`       | CSV soubor obsahující vybraná data pro generování promptů. Obsahuje přirozeně formulované dotazy v angličtině, strojově přeložené češtině a lokalizované češtině, které jsou vstupem pro jazykový model při generování vizualizací.      |

##Instalace

Pro spuštění pipeline je potřebné přidat vlastní .env soubor s API klíčem do OpenAI API (OPENAI_API_KEY=).

###Knihovny

<pre> ```python pip install openai
pip install pandas
pip install matplotlib``` </pre>
