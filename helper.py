#!/opt/homebrew/bin/python3.10

##############################
# 
# How to make me executable
#
# $ chmod u+x helper.py
# $ ln -s "$PWD/helper.py" /usr/local/bin/kk
#
# Usage:
# $ kk
#
# Voilà
# 
# Don't forget to remove the simbolic link after:
# $ unlink /usr/local/bin/kk

import os
import sys
import time

REPOSITORY_FOLDER_NAME = "repo"

def print_help():
    print("📖 Available commands:")
    commands = ["help", "clear", "init", "create <file content> <file name> <commit message>", "watch"]
    mapped = map(lambda el: "   - " + el, commands)
    print(*mapped, sep='\n')
    print("\n👉 Usage: %s init" %(sys.argv[0]))

def check_command_passed():
    if len(sys.argv) > 1:
        return True

    print("✋ Missed command\n")
    print_help()
    return False

def read_command():
    return sys.argv[1]

def clear():
    os.system("rm -rf ./" + REPOSITORY_FOLDER_NAME)
    print(f"🧹 Repository folder \"%s\" removed" %(REPOSITORY_FOLDER_NAME))

def init():
    os.system("mkdir ./" + REPOSITORY_FOLDER_NAME)
    os.system("cd ./%s && git init"%(REPOSITORY_FOLDER_NAME))
    print(f"\n👶 Repository created in folder \"%s\"" %(REPOSITORY_FOLDER_NAME))

def create(content, file_name, commit_message):
    print("📝 Creating new file and committing it")
    if content is None:
        content = input("   → File content: ")

    if file_name is None:
        default_file_name = content + ".txt"
        file_name = input("   → File name (leave empty for use \"%s\"): " %(default_file_name))
        if file_name == "":
            file_name = default_file_name

    if commit_message is None:
        default_commit_message = content
        commit_message = input("   → Commit message (leave empty for use \"%s\"): " %(default_commit_message))
        if commit_message == "":
            commit_message = default_commit_message

    print(f"\nCreating file \"%s\" with content \"%s\" and commit it with message \"%s\"" %(file_name, content, commit_message))
    os.system("echo %s > %s" %(content, file_name))
    os.system("git add " + file_name)
    os.system("git commit -m " + commit_message)

def watch():
    clear = lambda: os.system('clear')
    while True:
        clear()
        os.system("git --no-pager log --all --decorate --oneline --graph")
        time.sleep(2)

def handle_command(command):
    match command:
        case "help":
            print_help()
       
        case "clear":
            clear()
       
        case "init":
            init()
        
        case "create":
            content = sys.argv[2] if len(sys.argv) >= 3 else None
            file_name = sys.argv[3] if len(sys.argv) >= 4 else None
            commit_message = sys.argv[4] if len(sys.argv) >= 5 else None

            if content is not None:
                if file_name is None:
                    file_name = "%s.txt" %(content)
                
                if commit_message is None:
                    commit_message = content

            create(content, file_name, commit_message)
       
        case "watch":
            watch()
        
        case _:
            print("Unknown command")
            print_help()

#---------------------------------------------------------
if check_command_passed() == False:
    exit(1)

command = read_command()

handle_command(command)