from rich.console import Console

console = Console()

def show_banner():
    console.print(r"""
    ___  ________  ________  _______      
   |\  \|\   __  \|\   ___ \|\  ___ \     
   \ \  \ \  \|\  \ \  \_|\ \ \   __/|    
 __ \ \  \ \   __  \ \  \ \\ \ \  \_|/__  
|\  \\_\  \ \  \ \  \ \  \_\\ \ \  \_|\ \ 
\ \________\ \__\ \__\ \_______\ \_______\
 \|________|\|__|\|__|\|_______|\|_______|
[bold blue]Just A Daily Executive • Initiating mission protocol...[/bold blue]
""", style="bold white on black")
