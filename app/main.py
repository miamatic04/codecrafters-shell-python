import sys

def echo(text):
    print(text)


def main():
    while(True):
        sys.stdout.write("$ ")
        command = input()
        if (command == "exit"):
            break
        elif (command[0:4] == "echo"):
            echo(command[5:])
        else:
            print(f'{command}: command not found')
    pass


if __name__ == "__main__":
    main()
