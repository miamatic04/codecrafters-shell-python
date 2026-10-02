import sys
import shutil
import subprocess
import pathlib
import os
import re

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
        command_exe, *rest = command.split(' ', 1)
        args = rest[0] if rest else ""

        pattern1 = '([^ \']+)' 
        pattern2 = '\'([^\']*)\'' 

        tokens = [m1 or m2 for m1, m2 in re.finditer(pattern1 + '|' + pattern2, args)]

        prev_end = None
        for m in re.finditer(pattern1 + '|' + pattern2, args):
            content = m.group(1) or m.group(2)
            if prev_end is not None and m.start() == prev_end:
                tokens[-1] += content
            else:
                tokens.append(content)
            prev_end = m.end()

        args = ' '.join(tokens)

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
