import sys


def main():
    while True:

    # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

    # Wait for user input
        command = input()
        if command() == "exit 0":
            sys.exit(0)

        print(f"{command}: command not found")



if __name__ == "__main__":
    main()
