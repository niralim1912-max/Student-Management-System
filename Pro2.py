while True:
    print("1 Add Student")
    print("2 View Students")
    print("3 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        with open("students.txt", "a") as file:
            file.write(name + "\n")
        print("Student added successfully")

    elif choice == "2":
        print("Student List:")
        with open("students.txt", "r") as file:
            data = file.read()
            print(data)

    elif choice == "3":
        print("Exiting...")
        break   # Loop stop karne ke liye zaroori hai

    else:
        print("Invalid choice")
