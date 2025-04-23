# ai_assiistant.py

import os
from dotenv import load_dotenv
from rich.console import Console
from openai import OpenAI  # ✅ works on SDK >= 1.14.x

console = Console()
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_task():
    prompt = (
        "Suggest one high-impact task I can do right now in cybersecurity "
        "training or a 30-minute workout. Be concise."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    suggestion = response.choices[0].message.content.strip()
    console.print(f"\n[bold green]🧠 AI Suggestion:[/bold green] {suggestion}")
