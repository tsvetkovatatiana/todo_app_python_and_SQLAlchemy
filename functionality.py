import os

from database import Note, User, UserNote, Session

# Tracking logged-in user
current_user_id = 0


def register():
    global current_user_id
    print("Registration ======================================================================")

    while True:
        with Session() as session:
            print("Your username: ")
            username = input().strip()
            print("Your password: ")
            password = input()
            if not username or not password:
                print("Username and password cannot be empty. Please try again.")
                continue

            # checking if username exist
            user_found = session.query(User).filter(User.username == username).first()
            if user_found:
                print("This username is already taken. Try another one:)")
                continue
            else:
                new_user = User(username=username, password=password)
                session.add(new_user)
                session.commit()
                session.refresh(new_user)

                print("Now you are in the system ===================================================================")
                current_user_id = new_user.userId
                break


def login():
    global current_user_id

    print("Login ======================================================================")

    while True:
        with Session() as session:
            print("Your username: ")
            username = input().strip()

            user = session.query(User).filter(User.username == username).first()

            if user is None:
                print("Wrong username. Try again or create a new account")
                print("1: Try again")
                print("2: Register")

                while True:
                    try:
                        selection = int(input().strip())
                        if selection == 1:
                            break
                        elif selection == 2:
                            register()
                            return
                        else:
                            print("Invalid option. Please enter 1 or 2.")
                    except ValueError:
                        print("Oops! Invalid entrance. Try again")
                        continue

                continue

            print("Your password: ")
            password = input()

            if user.password == password:
                print(f"Login successful! Welcome, {username} =======================================================")
                current_user_id = user.userId
                return
            else:
                print("Password is incorrect. Try again.")
                continue


def show_notes():
    global current_user_id
    print("Yours TODOs: ======================================================================")

    with Session() as session:
        notes = session.query(Note).join(UserNote).filter(
            (Note.ownerId == current_user_id) | (UserNote.userId == current_user_id)).all()

        if len(notes) < 1:
            print("Empty. You should add some notes first.")
            return

        for note in notes:
            note_id = note.noteId
            note_name = note.name
            note_description = note.description
            note_owner = note.owner.username
            time_added = note.timeAdded
            print(f"""{os.linesep}– {note_id}: {note_name}
            – Description: {note_description}
            – Owner: {note_owner}
            – Time Added: {time_added.strftime('%Y-%m-%d %H:%M')}
            """)

    print("======================================================================" + os.linesep)


def create_note():
    global current_user_id
    print("Creating a note ======================================================================")
    print("Name of the note: ")
    note_name = input()

    description = None

    while True:
        print("Do you want to enter description to your note (Y|N): ")
        try:
            selection = input().strip().lower()
            if selection == "y":
                print("Enter description: ")
                description = input()
                break
            elif selection == "n":
                break

        except ValueError:
            print("Invalid entrance. Try again")

    with Session() as session:
        new_note = Note(name=note_name, description=description, ownerId=current_user_id)
        session.add(new_note)
        session.commit()
        print("Note created successfully! ==============================================================")

        # Adding entry to associative table userNotes
        user_note_entry = UserNote(userId=current_user_id, noteId=new_note.noteId)
        session.add(user_note_entry)
        session.commit()


def remove_note():
    with Session() as session:
        notes = session.query(Note).filter(Note.ownerId == current_user_id).all()

        if not notes:
            print("Empty. You should add some notes first.")
            return

        print("Give Id to remove: ")
        try:
            note_id = int(input().strip())
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        note_to_remove = session.query(Note).filter(Note.noteId == note_id, Note.ownerId == current_user_id).first()
        if note_to_remove:
            session.delete(note_to_remove)
            session.commit()
            print("Note was removed ================================================================")
        else:
            print("Invalid Id")
