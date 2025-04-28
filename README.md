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

