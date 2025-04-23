import subprocess
from datetime import datetime
from rich.console import Console
from pathlib import Path
import threading

console = Console()
LOGS_DIR = Path("jade/logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

def log_output(process, log_file):
    for line in process.stdout:
        log_file.write(line)
        log_file.flush()

def run_and_log(command: list, note: str = ""):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = LOGS_DIR / f"{timestamp}.md"

    try:
        console.print(f"[bold blue]▶️ Running command:[/bold blue] {' '.join(command)}\n")

        with open(log_path, "w", encoding="utf-8") as log_file:
            log_file.write(f"# 🗂️ Command Log - {timestamp}\n\n")
            log_file.write(f"**Command:** `{' '.join(command)}`  \n")
            log_file.write(f"**Note:** {note if note else 'N/A'}  \n\n## 📄 Output:\n\n")

            # Run the command through the shell for Windows compatibility
            process = subprocess.Popen(
                " ".join(command),  # Join the command list into a string
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                shell=True  # Use shell=True to handle Windows built-ins like echo
            )

            thread = threading.Thread(target=log_output, args=(process, log_file))
            thread.start()
            thread.join()

        console.print(f"\n[green]✅ Command execution completed! Output is logged to[/green]\n{log_path}")

    except Exception as e:
        console.print(f"[red]❌ Failed to run command:[/red] {e}")
