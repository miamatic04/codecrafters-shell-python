import sys
import shutil
import subprocess

def echo(text):
    print(text)

def type(command):
    if command in ['echo', 'exit', 'type']:
        print(f'{command} is a shell builtin')
    elif path := shutil.which(command):
        print(f'{command} is {path}')
    else:
        print(f'{command}: not found')


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
        else:
            print(f'{command}: command not found')
    pass


if __name__ == "__main__":
    main()
