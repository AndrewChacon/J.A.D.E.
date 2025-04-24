import typer
import shlex
from rich.console import Console
from jade.command_logger import run_and_log
from jade.banner import show_banner
from jade.timer import start_timer
from jade.todo import todo_prompt

console = Console()

def greet():
    show_banner()
    console.print("[green]✅ Systems check complete.[/green] Ready to serve, [bold]Drew[/bold].")
    console.print("[cyan]🛡️ Phase 6: Theming & Identity engaged...[/cyan]\n")

def main_loop():
    greet()
    console.print("[bold yellow]Type a command: [green]brief[/green], [green]suggest[/green], [green]execute[/green], [green]run-cmd[/green], [green]todo[/green], [green]timer[/green], or [red]exit[/red][/bold yellow]\n")
    
    while True:
        command = typer.prompt(">>").strip()

        if command.lower() == "brief":
            console.print("[green]✅ Brief functionality will go here[/green]")
        elif command.lower() == "suggest":
            console.print("[green]✅ Suggest functionality will go here[/green]")
        elif command.lower().startswith("execute"):
            task = command[7:].strip()
            if task:
                console.print(f"[green]✅ Focus session started with task: {task}[/green]")
            else:
                console.print("[red]⚠️ Please include a task after 'execute'.[/red]")
        elif command.lower().startswith("run-cmd"):
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
        elif command.lower() in ["exit", "quit"]:
            console.print("[bold red]👋 Shutting down. Catch you later, Drew.[/bold red]")
            break
        else:
            console.print("[yellow]❓ Unknown command.[/yellow] Try: brief, suggest, execute, run-cmd, timer, todo, or exit.")

if __name__ == "__main__":
    main_loop()
