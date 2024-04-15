import os
import subprocess
import time
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

def find_ansible_directory():
    for root, dirs, files in os.walk('/'):
        if 'ansible' in dirs:
            return os.path.join(root, 'ansible', 'menu')  # Assuming 'menu' subdir is under 'ansible'
    return None

def display_logo(ansible_dir):
    logo_path = os.path.join(ansible_dir, 'logo.txt')
    with open(logo_path, 'r') as file:
        print(Panel.fit(Text(file.read(), style="bold cyan")))
    time.sleep(2)

def banner(ansible_dir):
    banner_path = os.path.join(ansible_dir, 'banner.txt')
    with open(banner_path, 'r') as file:
        print(Panel.fit(Text(file.read(), style="bold cyan")))
    agreement_text = Text("Type 'AGREE' to continue: ", style="bold cyan")
    agreement = input(agreement_text)
    if agreement.lower() != 'agree':
        print(Panel.fit(Text("You did not agree. Exiting.", style="bold magenta")))
        exit()
    else:
        print(Panel.fit(Text("You agreed. Continuing to the menu.", style="bold bright_green")))
        activate_and_change_dir()

def activate_and_change_dir():
    subprocess.call("source /nmb/Environments/ansible/bin/activate", shell=True)
    os.chdir("/nmb/rcce-ansible")

def confirm_and_execute(option_function):
    confirmation_text = Text(f"Are you sure? Type 'Yes' to run {option_function.__name__} on the entire network! ", style="bold magenta")
    confirmation = input(confirmation_text)
    while confirmation.lower() not in ['yes', 'no']:
        print("You MUST type 'Yes' or 'No'!")
        confirmation = input(confirmation_text)
    if confirmation.lower() == 'yes':
        option_function()
    else:
        print("Operation canceled, returning to menu.")

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

def option_10():
    result = subprocess.check_output(['echo', "This is a placeholder for menu option 10 function"], text=True)
    print(result)
    time.sleep(1)
# Similar function implementations for option_2 to option_9

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
            else:
                confirm_and_execute(globals()[f'option_{choice}'])
        else:
            print(Panel.fit(Text("You must make a valid selection 1-10!", style="bold magenta")))

def main():
    ansible_dir = find_ansible_directory()
    if ansible_dir is None:
        print("Ansible directory not found, exiting.")
        return
    display_logo(ansible_dir)
    banner(ansible_dir)
    menu()

if __name__ == "__main__":
    main()
