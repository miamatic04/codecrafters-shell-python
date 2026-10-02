import sys

def echo(text):
    print(text)

def type(command):
    if command in ['echo', 'exit', 'type']:
        print(f'{command} is a shell builtin')
    else:
        print(f'{command}: not found')


def main():
    while(True):
        sys.stdout.write("$ ")
        command = input()
        if (command == "exit"):
            break
        elif (command[0:4] == "echo"):
            echo(command[5:])
        elif (command[0:4] == "type"):
            type(command[5:])
        else:
            print(f'{command}: command not found')
    pass


if __name__ == "__main__":
    main()
