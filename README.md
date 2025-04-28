# VisEvalCzech
## Struktura a popis hlavních podsložek a souborů repozitáře VisEvalCzech

Repozitář **VisEvalCzech** obsahuje českou lokalizaci benchmarku VisEval pro hodnocení schopností LLMs generovat vizualizace na základě přirozeného jazyka. Níže je popsána struktura hlavních složek a klíčových souborů, s důrazem na jejich funkci.

---

## Hlavní složky a soubory

| Název            | Popis                                                                                       |
|------------------|--------------------------------------------------------------------------------------------|
| `databases/`     | Obsahuje data, která slouží jako zdroj pro dotazy v benchmarku. Každá podsložka odpovídá jedné databázi, uvnitř které se nachází soubory s ukázkovými daty. Tyto databáze jsou základem pro generování a ověřování vizualizačních dotazů. |
| `graphs/`        | Složka určená pro ukládání vizualizačních výstupů (vygenerované grafy ve formátu obrázků). Umožňuje porovnávat výstupy různých systémů nebo modelů. |
| `responses/`     | Obsahuje odpovědi modelů na jednotlivé dotazy benchmarku. Najdeme výstupy LLMs v různých jazykových verzích, případně i referenční odpovědi. Slouží k evaluaci přesnosti a interpretovatelnosti generovaných vizualizací. |
| `README.md`      | Hlavní dokumentace repozitáře. Stručně popisuje účel projektu, jeho strukturu a základní instrukce pro použití. Obsahuje také informace o původu dat a odkazy na metodologii lokalizace. |
| `LICENSE`        | Licenční podmínky projektu (MIT License), které umožňují volné použití a úpravy dat. |

---

## Popis klíčových souborů a skriptů

- **validace.xlsx**  
  Obsahuje podrobné porovnání výsledků experimentu. Slouží k dokumentaci a analýze přesnosti, interpretovatelnosti a dalších kvalitativních parametrů vygenerovaných vizualizací v jednotlivých jazykových verzích. Umožňuje přehledné srovnání úspěšnosti modelu v různých scénářích podle metodiky popsané v práci.

- **run.py**  
  Jednoduchý spouštěcí skript, který slouží k inicializaci a řízení běhu hlavního experimentu. Volá hlavní funkci a nastavuje základní parametry běhu.

- **generate_from_queries_final.py**  
  Hlavní skript projektu, ve kterém jsou definovány specifikace a konfigurace použitého jazykového modelu. Obsahuje kompletní logiku pro generování vizualizačních výstupů na základě vstupních dotazů, zpracování promptů, manipulaci s vygenerovanými hodnotami a případné ukládání výsledků. Tento skript je jádrem celé experimentální pipeline a umožňuje detailní nastavení parametrů generování.

- **nl_queries_selected.csv**  
  CSV soubor obsahující vybraná data pro generování promptů. Obsahuje přirozeně formulované dotazy v angličtině, strojově přeložené češtině a lokalizované češtině, které jsou vstupem pro jazykový model při generování vizualizací. Slouží jako základní datová sada pro testování a evaluaci schopností modelu.

