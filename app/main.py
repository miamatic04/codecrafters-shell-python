import sys
import shutil
import subprocess
import pathlib
import os

def echo(text):
    print(text)

def type(command):
    if command in ['echo', 'exit', 'type', 'pwd', 'cd']:
        print(f'{command} is a shell builtin')
    elif path := shutil.which(command):
        print(f'{command} is {path}')
    else:
        print(f'{command}: not found')

def pwd():
    print(pathlib.Path().resolve())

def cd(new_path):
    if new_path.startswith("/"):
        if os.path.exists(new_path) and os.path.isdir(new_path):
            os.chdir(new_path)
        else:
            print(f"cd: {new_path}: No such file or directory")
    else:
        print(f'cd: {new_path}: No such file or directory')

def main():
    while(True):
        sys.stdout.write("$ ")
        command = input()
        command_exe = command.split(' ', 1)[0]
        if (command == "exit"):
            break
        elif (command[0:4] == "echo"):
            echo(command[5:])
        elif (command[0:4] == "type"):
            type(command[5:])
        elif(shutil.which(command_exe)):
            subprocess.run(command.split(' '))
        elif(command[0:3] == "pwd"):
            pwd()
        elif (command[0:2] == "cd"):
            cd(command[3:])
        else:
            print(f'{command}: command not found')
    pass


if __name__ == "__main__":
    main()
