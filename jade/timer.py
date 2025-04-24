import time
from rich.console import Console

console = Console()

def start_timer(minutes: int):
    seconds = minutes * 60
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            console.print(f"⏳ {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            seconds -= 1
        console.print("\n[green]✅ Time's up! Break or shift gears.[/green]")
    except KeyboardInterrupt:
        console.print("\n[red]⏹️ Timer canceled[/red]")