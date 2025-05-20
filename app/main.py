import sys

builtins = {"echo", "exit", "type"}
def main():
    while True:

    # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

    # Wait for user input
        command = input()

        if command.startswith("echo"):
            print(command[5:])
        elif command.startswith("exit"):
            sys.exit(0)
        elif command.startswith("type"):
             i = command[5:]
             if i in builtins:
                 print(f"{command} is a shell builtin")
             else:
                 print(f"{command}: command not found")
        else:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()
