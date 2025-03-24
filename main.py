import sys
import os

items = []
current_item_id = 0


def show_items():
    print("Yours TODOs: ")
    print("-------------")

    if len(items) < 1:
        print("There is no todo's yet")
        return

    for item in items:
        item_id = item['id']
        item_name = item['name']
        print(f"{item_id}: {item_name}")
    print("-------------" + os.linesep)

def create_item():
    global current_item_id
    print("Name of the item: ")
    item_name = input()

    current_item_id = current_item_id + 1
    item = {
        "name": item_name,
        "id": current_item_id
    }
    items.append(item)
    print("Item was created")

def remove_item():
    if len(items) < 1:
        print("You should add some items first.")
        return

    print("Give Id to remove: ")
    item_id = int(input())

    item_index = None

    for index, item in enumerate(items):
        if item['id'] == item_id:
            item_index = index

    if item_index is not None:
        items.pop(item_index)
        print("Item was removed")
    else:
        print("Invalid ID")



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