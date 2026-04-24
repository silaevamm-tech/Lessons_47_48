notes = []

# Create
# Read
# Update
# Delete
while True:
    command = str(input("Enter a command : "))
    # Create
    if command == "c1":
        # 1
        note = str(input("Enter a note: "))
        notes.append(note)
    elif command == "c2":
        # 2
        note = str(input("Enter a note: "))
        notes.insert(0, note)
    # Read
    elif command == "r1":
        # 1
        for note in notes:
            print(note)
    elif command == "r2":
        # 2
        for i in range(len(notes)):
            print(i, notes[i])
    # Update
    elif command == "u1":
        # 1
        index = int(input("Enter an index : "))
        new_note = str(input("Enter a new note : "))
        notes[index] = new_note
    elif command == "u2":
        # 2 По повному збігу старого напису
        old_note = str(input("Enter a note : "))
        new_note = str(input("Enter a new note : "))
        for i in range(len(notes)):
            if old_note == notes[i]:
                notes[i] = new_note
    elif command == "u3":
        # 3 По частковому збігу старого напису
        old_note = str(input("Enter a note : "))
        new_note = str(input("Enter a new note : "))
        for i in range(len(notes)):
            if old_note in notes[i]:
                notes[i] = new_note
                # Delete
    elif command == "d1":
        # 1
        index = int(input("Enter an index : "))
        del notes[index]
    elif command == "d2":
        # 2 По повному збігу старого напису
        old_note = str(input("Enter a note : "))
        for i in range(len(notes)):
            if old_note == notes[i]:
                del notes[i]
    elif command == "d3":
        # 3 По частковому збігу старого напису
        old_note = str(input("Enter a note : "))
        for i in range(len(notes)):
            if old_note in notes[i]:
                del notes[i]