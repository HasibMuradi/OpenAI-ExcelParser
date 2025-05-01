# Entwicklung eines flexiblen Datenkonverters

Entwickle ein Python-Programm, das Excel-Dateien mit Zeitreihen und Metadaten mit Hilfe der OpenAI API in ein einheitliches Zielformat konvertiert.

Du erhältst vier Excel-Dateien, die jeweils eine Zeitreihe mit Metadaten enthalten. Jede Datei hat ein leicht abweichendes Format.

## Aufgabe

- Definiere ein einheitliches Zielformat als Python-Datenstruktur, das sowohl die Zeitreihe als auch deren Metadaten aufnehmen kann.

- Entwickle ein Python-Programm, das folgende Funktionen erfüllt:
  - Einlesen einer Excel-Datei
  - Senden der Daten der eingelesenen Datei an die OpenAI API
  - Speichern der von OpenAI “geparsten” Daten in das definierte Zielformat
  - Ausgabe der Zeitreihe und deren Metadaten

Im Wesentlichen handelt es sich also um einen Parser, der mit unscharfen (fuzzy) Eingaben umgehen kann.

- Stelle dein Projekt als Git-Repository auf Github, Gitlab oder einem ähnlichen Dienst nicht-öffentlich für uns bereit und gibt uns Zugang zu dem Repository

## Hinweise

Nutze das Konzept von [Structured output from LLMs](https://www.thoughtworks.com/radar/techniques/structured-output-from-llms). Weitere Informationen findest du z.B. unter:

- [Structured Outputs - OpenAI Platform](https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses)
- [Structured data extraction from unstructured content using LLM schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/#structured-data-extraction-is-a-killer-app-for-llms)

Falls du während der Umsetzung auf Hindernisse stößt, ist dies kein Problem. Reiche den Stand ein, bis zu dem du gekommen bist und beschreibe die aufgetretenen Hindernisse.
