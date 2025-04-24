import typer
from rich.console import Console
from rich.table import Table
from pathlib import Path

console = Console()
TODO_FILE = Path("jade/data/todo.txt")
TODO_FILE.parent.mkdir(parents=True, exist_ok=True)

def show_todo_commands():
    console.print("\n[bold green]🧪 TODO Commands[/bold green]")
    console.print("[cyan]add[/cyan] - Add a new todo item")
    console.print("[cyan]list[/cyan] - View all todo items")
    console.print("[cyan]remove[/cyan] - Remove a todo item by number")
    console.print("[cyan]check[/cyan] - Mark a todo item as done or undone")
    console.print("[cyan]clear[/cyan] - Wipe all todo items")
    console.print("[cyan]exit[/cyan] - Exit todo menu")
    console.print("[cyan]help[/cyan] - Show this help menu\n")

def add_todo():
    item = typer.prompt("📝 What would you like to add?")
    with open(TODO_FILE, "a", encoding="utf-8") as f:
        f.write(f"{item}|0\n")  # 0 = incomplete
    console.print(f"[green]✅ Added:[/green] {item}")

def list_todos():
    if TODO_FILE.exists():
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if '|' in line]

        if lines:
            table = Table(title="📋 Your Todo List", show_header=True, header_style="bold magenta")
            table.add_column("No.", style="dim", width=6)
            table.add_column("Task")
            table.add_column("Status", justify="center")

            for idx, line in enumerate(lines, 1):
                item, status = line.split("|")
                emoji = "✅" if status == "1" else "❌"
                table.add_row(str(idx), item, emoji)

            console.print(table)
        else:
            console.print("[yellow]⚠️ No todo items found.[/yellow]")
    else:
        console.print("[yellow]⚠️ Todo list not found.[/yellow]")

def remove_todo():
    list_todos()
    number = typer.prompt("❌ Enter the number of the item to remove")
    try:
        number = int(number)
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if 0 < number <= len(lines):
            removed = lines.pop(number - 1)
            with open(TODO_FILE, "w", encoding="utf-8") as f:
                f.writelines(lines)
            console.print(f"[red]🗑️ Removed:[/red] {removed.split('|')[0]}")
        else:
            console.print("[red]❌ Invalid number.[/red]")
    except ValueError:
        console.print("[red]❌ Please enter a valid number.[/red]")

def check_todo():
    list_todos()
    number = typer.prompt("🔁 Enter the number to toggle its status")
    try:
        number = int(number)
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f]

        if 0 < number <= len(lines):
            item, status = lines[number - 1].split("|")
            new_status = "0" if status == "1" else "1"
            lines[number - 1] = f"{item}|{new_status}"
            with open(TODO_FILE, "w", encoding="utf-8") as f:
                f.write("\n".join(lines) + "\n")
            console.print(f"[cyan]🔁 Toggled:[/cyan] {item} → {'✅' if new_status == '1' else '❌'}")
        else:
            console.print("[red]❌ Invalid number.[/red]")
    except ValueError:
        console.print("[red]❌ Please enter a valid number.[/red]")

def clear_todos():
    if TODO_FILE.exists():
        TODO_FILE.write_text("")
        console.print("[red]🧼 All todo items cleared.[/red]")
    else:
        console.print("[yellow]⚠️ No todo file to clear.[/yellow]")

def todo_prompt():
    show_todo_commands()
    while True:
        action = typer.prompt("todo >", prompt_suffix=" ").strip().lower()
        if action == "add":
            add_todo()
        elif action == "list":
            list_todos()
        elif action == "remove":
            remove_todo()
        elif action == "check":
            check_todo()
        elif action == "clear":
            clear_todos()
        elif action in ["exit", "back", "quit"]:
            console.print("[bold red]⬅️ Exiting todo menu...[/bold red]\n")
            break
        elif action == "help" or action == "":
            show_todo_commands()
        else:
            console.print("[yellow]❓ Unknown command. Type 'help' to see the available commands.[/yellow]")
