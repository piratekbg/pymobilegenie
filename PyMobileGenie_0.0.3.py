import os
import itertools
from datetime import datetime as timestamp
from time import sleep as w8
from rich.progress import track
from rich import print as rprint
from rich.console import Console
from rich.spinner import Spinner as spin

#import program_variables as pv
console=Console()
program_version = "0.0.3"
first_timer = True

mobile_operators = {
				"A1": ["880","881","882","883","884","885","886","887","888","889"],
			"Vivacom": ["870","871","872","873","874","875","876","877","878","879"],
			"Yettel": ["890","891","892","893","894","895","896","897","898","899"]
}

def header_print(color1="yellow", color2="cyan", color3="cyan"):
	cP=color1
	cM=color2
	cG=color3
	cV="green"
	author = {"Professor Volt":"punkinfocode@gmail.com"}
	v = {"0.0.3":"12.04.2023"}
	title = str(f"""[bold red]##########################
##   [{cP}]Py[/{cP}][{cM}]Mobile[/{cM}][{cG}]Genie[/{cG}]	##
##		 [{cV}]v.{list(v)[0]}[/{cV}]##
##########################[/bold red]""")

	if(first_timer):
		rprint(title)
		w8(1)
		rprint(f"[bold]by [dark_red on white]{list(author)[0]}[/]\n[white on black]{author[list(author)[0]]}")
		w8(5)
		os.system("clear")
	else:
		os.system("clear")
		rprint(title)
		
	
def operator_selector():
	header_print("yellow","cyan",				"dark_blue")
	rprint(f"[bold underline red]Choose operator:[/]")
	#os.system("clear")
	selector = 1
	operator_name = ""
	for op in range(0, len(mobile_operators)):
		#print(op)
		operator_name = list(mobile_operators)[op]
		rprint(f"[bold cyan][[bold magenta]{op+1}[/bold magenta]][/bold cyan] ~[bold yellow] {operator_name}[/bold yellow]")
	user_input = input()
	operator = {
	list(mobile_operators)[int(user_input)-1]: mobile_operators[list(mobile_operators)[int(user_input)-1]]
	}
	return (operator)

def numbers_generator(prefixes, zero=False):
    mob_numbers = []
    for combination in track(itertools.product(range(10), repeat=6),
                             description="[bold green]Generating...[/]"):
        number = str("".join(map(str, combination)))
        [mob_numbers.append(p+number) for p in prefixes if zero==False]
        [mob_numbers.append("0"+p+number) for p in prefixes if zero==True]
        
        #mob_numbers.append(number)
    rprint(f"[blink bold cyan]Done![/]")
    w8(3)
    return mob_numbers

header_print("yellow","cyan","dark_blue")
first_timer = False
op_choice = operator_selector()
header_print("yellow","cyan","dark_blue")
rprint(f"[bold][red underline]You chose : [/red underline]\n[red]Operator:[/red]  [cyan]{list(op_choice)[0]}[/cyan]\n[red]Prefixes:[/red] [yellow]{[str(p) for p in list(op_choice[list(op_choice)[0]])]}[/yellow][/bold]")

numbers = numbers_generator(op_choice[list(op_choice)[0]])
#print(numbers)
header_print("yellow","cyan","dark_blue")
file_name = str(f"{list(op_choice)[0]}_numbers_export.txt")
rprint(f"Exporting to file {file_name}")
with open(file_name, "w") as f:
	for number in track(numbers, description="[bold green]Exporting...[/]"):
		f.write(number+"\n")
	f.close()
	

	