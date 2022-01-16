import helper

Person = {'name': "", 'number': 0}

running = True

def create_contact():
    print()
    Person['name'] = input("Enter the name : ").lstrip().rstrip().title()
    Person['number'] = int(input("Enter the number : "))

    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    all_contacts = helper.insert_contact(all_contacts, Person)
    all_contacts_string = helper.convert_contacts_to_string(all_contacts)
    open('contacts.txt', 'w').write(all_contacts_string)
    print('Contact Saved👍🏼')

def show_all_contacts():
    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    if not all_contacts:
        print('No contacts present🍂')
        return
    print("""
\t#####################################
\t\t    All Contacts
\t#####################################\n
\tSr.No.\t Name\t\t\tNumber""")
    helper.display(all_contacts)

def find_contact():
    name = input('Enter the name : ')
    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    results = helper.filter(all_contacts, name)
    if not results:
        print("\nNo Contacts with given name.😐")
        return
    print("""
\t#####################################
\t\tWe found these results
\t#####################################\n
\tSr.No.\t Name\t\t\tNumber""")
    helper.display(results)

def delete_contact():
    name = input('Enter the name : ')
    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    results = helper.filter(all_contacts, name)

    if not results:
        print('\nNo contacts with given name found😐')
        return
    
    if len(results) == 1:
        all_contacts.remove(results[0])
        all_contacts_string = helper.convert_contacts_to_string(all_contacts)
        open('contacts.txt', 'w').write(all_contacts_string)
        print('Contact removed👍🏼')
        return
    
    print("""
\t#####################################
\t\tWe found these results
\t#####################################\n
\tSr.No.\t Name\t\t\tNumber""")
    helper.display(results)
    choice = input('\nWhich one do you want to delete (Enter a serial number) : ')

    while (not choice.isnumeric()) or (int(choice) <= 0) or (int(choice) > len(results)):
        if not choice.isnumeric():
            print('Please provide a number!🥺\n')
        if choice.isnumeric() and (int(choice) <= 0 or int(choice) > len(results)):
            print('Please provide a valid serial number!🥺\n')
        choice = input('Which one do you want to delete (Enter a serial number) : ')
    
    all_contacts.remove(results[int(choice)-1])
    all_contacts_string = helper.convert_contacts_to_string(all_contacts)
    open('contacts.txt', 'w').write(all_contacts_string)
    print('Contact removed👍🏼')

def modify_name():
    name = input('Enter the name : ')
    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    results = helper.filter(all_contacts, name)

    if not results:
        print('\nNo contacts with given name found😐')
        return
    
    if len(results) == 1:
        prev_num = results[0]['number']
        all_contacts.remove(results[0])

        new_name = input('Enter the new name : ').title()
        Person = {'name': new_name, 'number':prev_num}

        all_contacts = helper.insert_contact(all_contacts, Person)

        all_contacts_string = helper.convert_contacts_to_string(all_contacts)
        open('contacts.txt', 'w').write(all_contacts_string)
        print('Contact Updated👍🏼')
        return
    
    print("""
\t#####################################
\t\tWe found these results
\t#####################################\n
\tSr.No.\t Name\t\t\tNumber""")
    helper.display(results)
    choice = input('\nWhich one do you want to delete (Enter a serial number) : ')

    while (not choice.isnumeric()) or (int(choice) <= 0) or (int(choice) > len(results)):
        if not choice.isnumeric():
            print('Please provide a number!🥺\n')
        if choice.isnumeric() and (int(choice) <= 0 or int(choice) > len(results)):
            print('Please provide a valid serial number!🥺\n')
        choice = input('Which one do you want to delete (Enter a serial number) : ')

    new_name = input('Enter the new name : ').title()
    Person = {'name': new_name, 'number': results[int(choice)-1]['number']}
    
    all_contacts.remove(results[int(choice)-1])

    all_contacts = helper.insert_contact(all_contacts, Person)
    all_contacts_string = helper.convert_contacts_to_string(all_contacts)
    open('contacts.txt', 'w').write(all_contacts_string)
    print('Contact Updated👍🏼')

def modify_number():
    name = input('Enter the name : ')
    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    results = helper.filter(all_contacts, name)

    if not results:
        print('\nNo contacts with given name found😐')
        return
    
    if len(results) == 1:
        prev_name = results[0]['name']
        all_contacts.remove(results[0])

        new_number = input('Enter the new number : ')
        while not new_number.isnumeric():
            print('Please provide a number🥺')
            new_number = input('Enter the new number : ')
        Person = {'name': prev_name, 'number':new_number}

        all_contacts = helper.insert_contact(all_contacts, Person)

        all_contacts_string = helper.convert_contacts_to_string(all_contacts)
        open('contacts.txt', 'w').write(all_contacts_string)
        print('Contact Updated👍🏼')
        return
    
    print("""
\t#####################################
\t\tWe found these results
\t#####################################\n
\tSr.No.\t Name\t\t\tNumber""")
    helper.display(results)
    choice = input('\nWhich one do you want to update (Enter a serial number) : ')

    while (not choice.isnumeric()) or (int(choice) <= 0) or (int(choice) > len(results)):
        if not choice.isnumeric():
            print('Please provide a number!🥺\n')
        if choice.isnumeric() and (int(choice) <= 0 or int(choice) > len(results)):
            print('Please provide a valid serial number!🥺\n')
        choice = input('Which one do you want to delete (Enter a serial number) : ')

    new_number = input('Enter the new number : ')
    while not new_number.isnumeric():
        print('Please provide a number🥺')
        new_number = input('Enter the new number : ')

    Person = {'name': results[int(choice)-1]['name'], 'number': int(new_number)}
    
    all_contacts.remove(results[int(choice)-1])

    all_contacts = helper.insert_contact(all_contacts, Person)
    all_contacts_string = helper.convert_contacts_to_string(all_contacts)
    open('contacts.txt', 'w').write(all_contacts_string)
    print('Contact Updated👍🏼')

while running:
    print("""
1. Create a new contact
2. View all contacts
3. Find a contact
4. Delete a contact
5. Modify a name
6. Modify a number
7. Exit
    """)

    try:
        choice = int(input("Enter your choice : "))

        if choice == 1:
            create_contact()

        elif choice == 2:
            show_all_contacts()

        elif choice == 3:
            find_contact()

        elif choice == 4:
            delete_contact()

        elif choice == 5:
            modify_name()

        elif choice == 6:
            modify_number()

        elif choice == 7:
            running = False

        else:
            print("Invalid Choice")

    except:
        print('Wrong Input! Try again💥💥')
        print('')
        continue
    print('')
