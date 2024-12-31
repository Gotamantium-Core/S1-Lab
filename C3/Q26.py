'''
Create a telephone directory using a dictionary. The name of the individual and the
telephone number will be key and value, respectively. Write a Python program that
allows the user to perform the following operations:
(a) Add a Contact: Add a new contact with a name and phone number to the directory.
(b) Update a Contact: Update the phone number of an existing contact.
(c) Delete a Contact: Remove a contact from the directory.
(d) Search for a Contact: Look up the phone number of a contact by their name.
(e) Display All Contacts: Print all contacts in the directory.
(f) Exit the program.
Use a menu-driven approach
'''
telephoneNumbers = {} # directory


while True:
    print("--"*25)
    print("1. Add contact \n2. Update contact \n3. Delete contact \n4. Search for a contact \n5. Display contacts \n0. Exit")
    func = int(input("Enter function number: "))

    if func == 0: # close
        quit()
    elif func == 1: # add record
        name = input("Enter name: ")
        phno = int(input("Enter phone number: "))

        telephoneNumbers[name] = phno;

        print("Record added!")
    elif func == 2: # update record
        name = input("Enter name to be updated: ")

        try:
            phno = telephoneNumbers.pop(name)
            newName = input("Enter new name: ")
        except KeyError:
            print(f"{name} not found")
            continue

        telephoneNumbers[newName] = phno;
        print("Record updated!")
    elif func == 3: # remove record
        name = input("Enter name to be deleted: ")

        try:
            telephoneNumbers.pop(name)
            print("Record deleted!")
        except KeyError:
            print(f"{name} not found")
            continue
    elif func == 4: # show record
        name = input("Enter name: ")

        try:
            print(f"Name: {name} \nNumber: {telephoneNumbers[name]}")
        except KeyError:
            print(f"{name} does not exist")
            continue
    elif func == 5: # show all records
        for key, value in telephoneNumbers.items():
            print(f"{key} : {value}")
    else:
        print("Invalid function. Try again")
        