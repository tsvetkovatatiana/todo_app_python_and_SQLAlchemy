from functionality import *


def main():

    while True:
        print("======================================================================")
        print(f'''I will help you to remember all kind of things that you need to be done in one place.
                \nBut first you need to register or login to your existing account''')

        print("1. Register")
        print("2. Login")
        print("3: Exit" + os.linesep)
        try:
            selection = int(input())
            if selection == 1:
                register()
                break
            elif selection == 2:
                login()
                break
            elif selection == 3: sys.exit("Goodbye")
        except ValueError:
            print("Oops! Invalid entrance. Try again")


    while True:
        print(f"{os.linesep}What do you want to do today?")
        print("1: View todo notes")
        print("2: Create new to-do note")
        print("3: Remove note")
        print("4: Exit" + os.linesep)

        selection = input()
        if selection == "1": show_notes()
        if selection == "2": create_note()
        if selection == "3": remove_note()
        if selection == "4": sys.exit("Goodbye")


if __name__ == '__main__':
    print("======================================================================")
    print("Welcome to HOLDON to do list!")
    main()