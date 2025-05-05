import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv


def parse_with_openai(df: pd.DataFrame) -> str:

    subset = df.head(12)
    excel_to_csv = subset.to_csv(index=False)
    print("Excel data to parse:")
    print(excel_to_csv)

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found!")

    client = OpenAI(
        api_key=api_key
    )

    system_prompt = (
        "Du bist ein präziser Parser für Zeitreihendaten aus CSV-Dateien.\n"
        "Deine Aufgabe ist es, Zeitstempel und zugehörige Werte aus Tabellen zu extrahieren.\n\n"
        "Gib ausschließlich eine Liste im CSV-Format zurück, z.B.:\n"
        "2025-03-01 00:00:00, 2323894.6\n"
        "2024-01-01 00:00:00,00:15:00, 0\n"
        "oder andere Zeitformaten\n\n"
        "Regeln:\n"
        "- Erkenne Zeitinformationen, egal ob sie als Einzelspalte ('Zeit von') oder als Kombination von 'Zeit von' und 'Zeit bis' erscheinen.\n"
        "- Werte müssen Fließkommazahlen sein (z.B. 1234.56).\n"
        "- Gib nur gültige Zeit-Wert-Paare zurück.\n"
        "- Keine Kommentare, keine Erklärungen, keine Überschriften.\n"
        "- Keine Indizes, keine Zeilennummern.\n"
        "- Ignoriere leere, fehlerhafte oder unvollständige Zeilen.\n"
        "- Entferne alle Spalten wie 'Unnamed', leere Spalten oder irrelevante Metadaten.\n"
    )

    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": excel_to_csv}
        ]
    )
    content = completion.choices[0].message.content
    print("Successfully parsed excel data:")
    print(content + "\n")

    return content


