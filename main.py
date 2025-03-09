import os
from colorama import Fore, Style
import numpy as np
import platform
import psutil

def terminal():
    import os
    user_name = str(os.getlogin())
    computer_name = str(os.environ.get("COMPUTERNAME", os.uname().nodename if hasattr(os, 'uname') else "N/A"))
    intake_full = input(Fore.GREEN + user_name + Style.RESET_ALL + "@" + Fore.BLUE + computer_name + ":~" + Fore.WHITE + str(os.getcwd()) + " $ ")
    input_split = intake_full.split()
    intake = input_split[0]
    
    
    if intake == "exit":
        return
    elif intake == "ls":
        import os
        os.curdir
        print(os.listdir())
        terminal()
    elif intake == "pwd":
        import os
        print(os.getcwd())
        terminal()
    elif intake == "cd":
        import os
        path = input_split[1]
        os.chdir(path)
        terminal()
    elif intake == "touch":
        file = input_split[1]
        with open(file, "w") as f:
            f.write("")
        terminal()
    elif intake == "mkdir": 
        import os
        os.mkdir(input_split[1])
        terminal()
    elif intake == "rm":
        import os
        file = input_split[1]
        os.remove(file)
        terminal()
    elif intake == "rmdir":
        import os
        dir = input_split[1]
        os.rmdir(dir)
        terminal()
    elif intake == "cat":
        try:
            file = input_split[1]
            with open(file, "r") as f:
                print(f.read())
        except Exception as e:
            print("Bash error: cat: " + str(e))
        terminal()
    elif intake == "clear":
        import os
        os.system("cls")
        terminal()
    elif intake == "cls":
        import os
        os.system("cls")
        terminal()
    elif intake == "minz":
        import os
        os.system("root")
        terminal()
    elif intake == "fetchdev":
        print(Fore.BLUE + 
    """
    Fetching Dev...

                                      /__..-'''-.                                           
                                    '   _    \\ \                                      
    _..._   .--.                  /   /` '.   \\ \             __.....__        _..._    
    .'     '. |__|                 ./   |     \\  '  .--./)  .-''         '.    .'     '.  
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

              
        
        terminal()
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
    minz - Gives root permission in command.
    fetchdev - Fetches the device information.
""")
        
        terminal()
        import os
        os.path = "C:/Users"
    
    else:    
        print("""
Bash error: No Command Found
Command not found. Type 'help' to see the list of commands.
            """        
        )
        terminal()

terminal()