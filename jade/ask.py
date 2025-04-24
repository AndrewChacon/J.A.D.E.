import os
import openai
from rich.console import Console
from dotenv import load_dotenv

console = Console()
load_dotenv()

# Set up OpenAI client using the new 1.0.0+ interface
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_prompt():
    console.print("\n💬 Ask me anything! (type 'exit' to go back)")
    while True:
        user_input = input("ask > ").strip()
        if user_input.lower() in ["exit", "quit", "back"]:
            console.print("[bold red]⬅️ Leaving ask mode...[/bold red]\n")
            break

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            console.print(f"\n[bold green]🤖 Answer:[/bold green] {answer}\n")

        except Exception as e:
            console.print(f"[red]❌ Error:[/red] {e}")
