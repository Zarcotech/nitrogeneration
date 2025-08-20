import os
from colorama import Fore, Style
import platform
import psutil

def terminal():
    import os
    user_name = str(os.getlogin())
    computer_name = str(os.environ.get("COMPUTERNAME", os.uname().nodename if hasattr(os, 'uname') else "N/A"))
    os.chdir("C:/Users/" + user_name)
    while True:
        try:
            intake_full = input(Fore.GREEN + user_name + "@" + Fore.BLUE + computer_name + ":~" + Fore.WHITE + str(os.getcwd()) + " $ ")
            input_split = intake_full.split()
            intake = input_split[0]

            if intake == "exit":
                break
            elif intake == "ls":
                print(os.listdir())
            elif intake == "pwd":
                print(os.getcwd())
            elif intake == "cd":
                path = input_split[1]
                os.chdir(path)
            elif intake == "touch":
                file = input_split[1]
                with open(file, "w") as f:
                    f.write("")
            elif intake == "mkdir":
                os.mkdir(input_split[1])
            elif intake == "rm":
                file = input_split[1]
                os.remove(file)
            elif intake == "rmdir":
                dir = input_split[1]
                os.rmdir(dir)
            elif intake == "cat":
                file = input_split[1]
                with open(file, "r") as f:
                    print(f.read())
            elif intake == "clear":
                os.system("clear")
            elif intake == "cls":
                os.system("cls")
            elif intake == "mint":
                os.system("root")
            elif intake == "fetchdev":
                print(Fore.BLUE + """
                Fetching Dev...

                /__..-'''-.
                '   _    \\ \ 
                _..._   .--. /   /` '.   \\ \ __.....__ _..._ 
                .'     '. |__| ./   |     \\  '  .--./) .-'' '. .'     '. 
                .   .-.   ..--.     .|  .-,.--. |   '      |  '/.''\\\\  /     .-''"'-.  `. .   .-.   . 
                |  '   '  ||  |   .' |_ |  .-. |\\    \\     / /| |  | |/     /________\\   \\|  '   '  | 
                |  |   |  ||  | .'     || |  | | `.   ` ..' /  \\`-' / |                  ||  |   |  | 
                |  |   |  ||  |'--.  .-'| |  | |    '-...-'`   /("'`  \\    .-------------'|  |   |  | 
                |  |   |  ||  |   |  |  | |  '-                \\ '---. \\    '-.____...---.|  |   |  | 
                |  |   |  ||__|   |  |  | |                     /'""'.\\ `.             .' |  |   |  | 
                |  |   |  |       |  '.'| |                    ||     ||  `''-...... -'   |  |   |  | 
                |  |   |  |       |   / |_|                    \\' . __//                  |  |   |  | 
                '--'   '--'       `'-'                          `'---'                    '--'   '--' 

                CPU: """ + str(platform.processor()) + """
                OS: """ + str(platform.system()) + """
                RAM: """ + str(round(psutil.virtual_memory().total / (1024.0 **3))) + " GB" + """
                GPU: """ + str(platform.machine()) + """
                OS Version: """ + str(platform.version()) + """
                Python Version: """ + str(platform.python_version()) + """
                Python Compiler: """ + str(platform.python_compiler()) + """

                """ + Style.RESET_ALL)
            elif intake == "help":
                print("""
                List of Commands:
                help - Displays the list of commands.
                exit - Exits the terminal.
                ls - Lists all files in the directory.
                pwd - Displays the current directory.
                cd - Changes the directory.
                touch - Creates a file.
                mkdir - Creates a directory.
                rm - Removes a file.
                rmdir - Removes a directory.
                cat - Displays the contents of a file.
                clear - Clears the terminal screen.
                mint - Gives root permission in command.
                fetchdev - Fetches the device information.
                """)
            else:
                print("""
                Bash error: No Command Found
                Command not found. Type 'help' to see the list of commands.
                """)
        except Exception as e:
            print(f"Bash error: {e}")

terminal()
