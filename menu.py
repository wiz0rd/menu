from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import subprocess
import time

def banner():
    with open('banner.txt', 'r') as file:
        print(Panel.fit(Text(file.read(), style="bold cyan")))
    agreement_text = Text("Type 'AGREE' to continue: ", style="bold cyan")
    agreement = input(agreement_text)
    if agreement.lower() != 'agree':
        print(Panel.fit(Text("You did not agree. Exiting.", style="bold magenta")))
        exit()
    else:
        print(Panel.fit(Text("You agreed. Continuing to the menu.", style="bold bright_green")))

def option_1():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 1 function"], text=True)
    print(result)
    time.sleep(1)

def option_2():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 2 function"], text=True)
    print(result)
    time.sleep(1)

def option_3():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 3 function"], text=True)
    print(result)
    time.sleep(1)

def option_4():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 4 function"], text=True)
    print(result)
    time.sleep(1)

def option_5():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 5 function"], text=True)
    print(result)
    time.sleep(1)

def option_6():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 6 function"], text=True)
    print(result)
    time.sleep(1)

def option_7():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 7 function"], text=True)
    print(result)
    time.sleep(1)

def option_8():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 8 function"], text=True)
    print(result)
    time.sleep(1)

def option_9():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 9 function"], text=True)
    print(result)
    time.sleep(1)

def menu():
    while True:
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Option", justify="center")
        table.add_column("Description")
        for i in range(1, 10):
            table.add_row(str(i), f"This is placeholder number {i}")
        table.add_row("10", "Quit")
        print(table)

        choice_text = Text("Choose an option: ", style="bold cyan")
        choice = input(choice_text)
        if choice.isdigit() and 1 <= int(choice) <= 10:
            if int(choice) == 10:
                print(Panel.fit(Text("Exiting.", style="bold magenta")))
                break
            elif int(choice) == 1:
                option_1()
            elif int(choice) == 2:
                option_2()
            elif int(choice) == 3:
                option_3()
            elif int(choice) == 4:
                option_4()
            elif int(choice) == 5:
                option_5()
            elif int(choice) == 6:
                option_6()
            elif int(choice) == 7:
                option_7()
            elif int(choice) == 8:
                option_8()
            elif int(choice) == 9:
                option_9()
        else:
            print(Panel.fit(Text("You must make a valid selection 1-10!", style="bold magenta")))

def main():
    banner()
    menu()

if __name__ == "__main__":
    main()
