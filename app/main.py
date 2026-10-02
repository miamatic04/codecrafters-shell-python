import sys
import shutil
import subprocess
import pathlib
import os
import shlex

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
    if not new_path or new_path == "~":
        new_path = pathlib.Path.home()
    else:
        new_path = pathlib.Path(new_path).expanduser()

    try:
        os.chdir(new_path)
    except FileNotFoundError:
        print(f"cd: {new_path}: No such file or directory")
    except NotADirectoryError:
        print(f"cd: {new_path}: Not a directory")
    except PermissionError:
        print(f"cd: {new_path}: Permission denied")

def main():
    while(True):
        sys.stdout.write("$ ")
        command = input()
        split = shlex.split(command)
        command_exe = split[0]
        args = split[1:] if split else ""

        if command_exe == "exit":
            break
        elif command_exe == "echo":
            echo(args)
        elif command_exe == "type":
            type(args)
        elif command_exe == "pwd":
            pwd()
        elif command_exe == "cd":
            cd(args)
        elif(shutil.which(command_exe)):
            subprocess.run(command.split(' '))
        else:
            print(f'{command}: command not found')


if __name__ == "__main__":
    main()
