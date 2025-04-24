import typer
import shlex
from rich.console import Console
from jade.command_logger import run_and_log
from jade.banner import show_banner
from jade.timer import start_timer
from jade.todo import todo_prompt
from jade.ask import ask_prompt  # 👈 Make sure this import is here

console = Console()

def greet():
    show_banner()
    console.print("[green]✅ Systems check complete.[/green] Ready to serve, [bold]Drew[/bold].")
    console.print("[cyan]🛡️ Phase 6: Theming & Identity engaged...[/cyan]\n")

def main_loop():
    greet()
    console.print("[bold yellow]Type a command: [green]run-cmd[/green], [green]todo[/green], [green]timer[/green], [green]ask[/green], or [red]exit[/red][/bold yellow]\n")
    
    while True:
        command = typer.prompt(">>").strip()

        if command.lower().startswith("run-cmd"):
            parts = command.split(' --note ')
            raw_cmd = parts[0].replace("run-cmd", "").strip()
            note = parts[1] if len(parts) > 1 else ""
            cmd = shlex.split(raw_cmd)

            if cmd:
                run_and_log(cmd, note)
            else:
                console.print("[red]⚠️ Please provide a command to run.[/red]")
        elif command.lower() == "timer":
            start_timer()
        elif command.lower() == "todo":
            todo_prompt()
        elif command.lower() == "ask":
            ask_prompt()
        elif command.lower() in ["exit", "quit"]:
            console.print("[bold red]👋 Shutting down. Catch you later, Drew.[/bold red]")
            break
        else:
            console.print("[yellow]❓ Unknown command.[/yellow] Try: run-cmd, todo, timer, ask, or exit.")

if __name__ == "__main__":
    main_loop()
