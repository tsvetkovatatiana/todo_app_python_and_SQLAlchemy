from functionality import *


def main():
    while True:
        print(f"{os.linesep}What do you want to do today?")
        print("1: View todo items")
        print("2: Create new todo item")
        print("3: Remove item")
        print("4: Exit" + os.linesep)

        selection = input()
        if selection == "1": show_items()
        if selection == "2": create_item()
        if selection == "3": remove_item()
        if selection == "4": sys.exit("Goodbye")


if __name__ == '__main__':
    print("Welcome to TODO LIST Maker VERSION 5550574.00")
    main()