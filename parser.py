import os
import json
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

def parse_with_deepseek(df: pd.DataFrame) -> list[dict]:
    first10 = df.head(10)
    content = first10.to_csv()
    print(content)

    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("API key not found.")

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    system_prompt = (
        "Du bist ein Parser. Extrahiere eine Zeitreihe im Format:\n"
        "[{\"timestamp\": \"2023-01-01T00:00:00\", \"value\": 42.0}, ...]"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content},
        ],
        stream=False
    )

    converted = response.choices[0].message.content
    try:
        return json.loads(converted)
    except json.JSONDecodeError as e:
        print("Error with response!")
        raise e