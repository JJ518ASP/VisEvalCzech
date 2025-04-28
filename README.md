# VisEvalCzech
## Struktura a popis hlavních podsložek a souborů repozitáře VisEvalCzech

Repozitář **VisEvalCzech** obsahuje českou lokalizaci benchmarku VisEval pro hodnocení schopností LLMs generovat vizualizace na základě přirozeného jazyka. Níže je popsána struktura hlavních složek a klíčových souborů, s důrazem na jejich funkci.

---

## Hlavní složky a soubory

| Název            | Popis                                                                                       |
|------------------|--------------------------------------------------------------------------------------------|
| `databases/`     | Obsahuje databázové schémata a případně i data, která slouží jako zdroj pro SQL dotazy v benchmarku. Každá podsložka odpovídá jedné databázi, uvnitř se nachází soubory s ukázkovými daty. Tyto databáze jsou základem pro generování a ověřování vizualizačních dotazů. |
| `graphs/`        | Složka určená pro ukládání vizualizačních výstupů (vygenerované grafy ve formátu obrázků). Umožňuje porovnávat výstupy různých systémů nebo modelů. |
| `responses/`     | Obsahuje odpovědi modelů na jednotlivé dotazy benchmarku. Najdeme výstupy LLMs v různých jazykových verzích, případně i referenční odpovědi. Slouží k evaluaci přesnosti a interpretovatelnosti generovaných vizualizací. |
| `README.md`      | Hlavní dokumentace repozitáře. Stručně popisuje účel projektu, jeho strukturu a základní instrukce pro použití. Obsahuje také informace o původu dat a odkazy na metodologii lokalizace. |
| `LICENSE`        | Licenční podmínky projektu (MIT License), které umožňují volné použití a úpravy dat. |

---

## Obecná charakteristika hlavních složek

- **databases/**  
  - Struktura: Podsložky pro každou databázi, uvnitř popis datových tabulek.
  - Účel: Zajišťuje referenční datovou základnu pro SQL dotazy, které jsou součástí jednotlivých úloh benchmarku.  
  - Využití: Při evaluaci modelů slouží k ověření, zda generované dotazy a vizualizace odpovídají skutečné struktuře a obsahu dat.

- **graphs/**  
  - Struktura: Může obsahovat podsložky podle typu grafu, modelu nebo experimentu.
  - Účel: Uchovává vygenerované vizualizace pro další analýzu a porovnání.
  - Využití: Umožňuje vizuální i automatizované srovnání výstupů různých modelů a jazykových verzí.

- **responses/**  
  - Struktura: Často členěná podle experimentu, modelu nebo jazykové varianty.
  - Účel: Zaznamenává odpovědi LLMs na jednotlivé dotazy benchmarku, včetně případných referenčních odpovědí.
  - Využití: Slouží jako podklad pro kvantitativní i kvalitativní evaluaci výstupů (např. přesnost, interpretovatelnost, estetika).

---

## Klíčové soubory v kořenovém adresáři

- **README.md**  
  - Přehled projektu, jeho účelu a základní struktury.
  - Instrukce k použití a odkazy na další zdroje (např. metodologii lokalizace).

- **LICENSE**  
  - Definuje právní rámec pro využití, úpravy a šíření dat v repozitáři.

---
