#!/usr/bin/python3

import os
import itertools
from datetime import datetime as timestamp
from time import sleep as w8
from rich.progress import track
from rich import print as rprint
from rich.console import Console

import program_variables as pv
console=Console()
program_version = "4.0.1"

os.system("clear")
program_header = (f"[on black][bold green]{pv.name}[/] [bold cyan]~[/] [bold red][/on black][on grey11]{pv.name_country_short}[italic dark_cyan]edition[/]  [bold dark_red]version:[/][bold italic blink on black]{program_version}[/]")
rprint(program_header)
w8(3)
rprint(f"[on black][dark_orange3]ProfessorVolt[/] [bold dim white]..::[/][[bold italic dim dark_cyan]punkinfocode@gmail.com[/]][bold dim white]::..[/][/]")
w8(3)
os.system("clear")
rprint(f"[yellow on black]{pv.info_short}[/]")


def operator_selector():
    os.system("clear")
    rprint(program_header)
    selector = 1
    operator = {}
    user_operator = {}
    for op in pv.settings['operator_names_prefixes']:
        rprint(f"[{selector}] - [bold]{op}[/b]")
        operator[selector] = op
        selector += 1
    user_operator = operator[int(input("Choose operator (or quit by pressing 'q'): "))] if operator != 'q' else os.system("exit")
    rprint(f"You choose: {user_operator}")
    rprint(f"Selecting operator... '[bold]{user_operator}[/b]'")
    return user_operator

def op_prefix_generator(operator):
    op_digits = []
    op_prefix = pv.settings['operator_names_prefixes'][operator]
    for digit in range(0,10):
        operator_prefix = str(0) + \
            str(pv.settings['country_prefixes']['Bulgaria']) + \
                str(pv.settings['operator_names_prefixes'][operator]) + \
                    str(digit)
        op_digits.append(operator_prefix)
    return op_digits

def numbers_generator():
    mob_numbers = []
    for combination in track(itertools.product(range(pv.settings['numbers_generation']['digits_upto_to_use']), repeat=pv.settings['numbers_generation']['number_lenght']),
                             description="[bold green]Generating..."):
        number = str(''.join(map(str, combination)))
        mob_numbers.append(number)
    return mob_numbers

def number_prefixer(prefixes, numbers):
    complete_numbers = []
    for num in numbers:
        for prefix in prefixes:
            final_number = str(prefix)+str(num)
            complete_numbers.append(final_number)
    return complete_numbers

operator = operator_selector()
prefixes = op_prefix_generator(operator)
rprint([p for p in prefixes])
numbers = numbers_generator()
complete_numbers = number_prefixer(prefixes, numbers)

def number_exporter(complete_numbers):
    file_name = f"{pv.settings['export_file']['filename_default_name']}{operator}_{timestamp.now():%d-%m-%Y.%H:%M}.{pv.settings['export_file']['filename_extension'][0]}"
    with open(file_name, "w") as export_file:
        for number in track(complete_numbers, description=f"[bold blue]Exporting to file: \
            [bold yellow]\n{file_name}[/bold yellow][/bold blue]"):
            export_file.write(f"{number}\n")
    rprint(f"[bold magenta][italic]Done!!![/]")
        

def number_printer(complete_numbers):
    rprint(f"Printing {len(complete_numbers)} numbers:")
    for i in track(range(len(complete_numbers)), \
        description=f"[blue]printing [bold green]{operator}[/bold green] ...[/blue]"):
        rprint(f"{complete_numbers[i]}")
        

#if(input("Should I print out all numbers generated? [Y]/[N]?") == "Y"):
#    number_printer(complete_numbers)
rprint(f"Export the results([italic green on black]{len(complete_numbers)}[/] numbers)..? [on black][bold dark_cyan][Y]/[bold dark_red][N][/]?")
export = input().capitalize()

if(export == 'Y' or export == 'y'):
    
    number_exporter(complete_numbers)
else:
    rprint(f"This was a waste of computing power! Next time export to a file!!!")
    os.system("exit")
    

    
    
#f"[green]exporting to file [bold yellow]{file_name}[/bold yellow]...[/green]"