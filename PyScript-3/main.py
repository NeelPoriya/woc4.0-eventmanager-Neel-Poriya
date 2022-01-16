import helper

Person = {'name': "", 'number': []}

running = True

def create_contact():
    print()
    name = input("Enter the name : ").lstrip().rstrip().title()
    number = (int(input("Enter the number : ")))
    Person = { 'name' : name, 'number': [number]}
    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    all_contacts = helper.insert_contact(all_contacts, Person)
    
    try:
        all_contacts_string = helper.convert_contacts_to_string(all_contacts)
        open('contacts.txt', 'w').write(all_contacts_string)
        print('Contact Saved👍🏼')
    except:
        print('🤯🤯🤯')

    

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
        if len(results[0]['number']) == 1:
            new_number = input('Enter the new number : ')
            while not new_number.isnumeric():
                print('Please provide a number🥺')
                new_number = input('Enter the new number : ')

            contact_ind = all_contacts.index(results[0])
            all_contacts[contact_ind]['number'] = [int(new_number)]

            all_contacts_string = helper.convert_contacts_to_string(all_contacts)
            open('contacts.txt', 'w').write(all_contacts_string)
            print('Contact Updated👍🏼')
            return

        ind = input("Which of the number will you like to update : ")
        while (not ind.isnumeric()) or int(ind)<=0 or int(ind)>len(results[0]['number']):
            print('Please provide a valid serial number🥺')
            ind = input("Which of the number will you like to update : ")

        ind = int(ind)-1
        new_number = input('Enter the new number : ')
        while not new_number.isnumeric():
            print('Please provide a number🥺')
            new_number = input('Enter the new number : ')

        contact_ind = all_contacts.index(results[0])
        all_contacts[contact_ind]['number'][ind] = int(new_number)

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

    choice = int(choice)-1
    if len(results[choice]['number']) == 1:
        new_number = input('Enter the new number : ')
        while not new_number.isnumeric():
            print('Please provide a number🥺')
            new_number = input('Enter the new number : ')

        Person = {'name': results[choice]['name'], 'number': [int(new_number)]}
        
        all_contacts.remove(results[choice])

        all_contacts = helper.insert_contact(all_contacts, Person)
        all_contacts_string = helper.convert_contacts_to_string(all_contacts)
        open('contacts.txt', 'w').write(all_contacts_string)
        print('Contact Updated👍🏼')
        return
    
    ind = input("Which of the number will you like to update : ")
    while (not ind.isnumeric()) or int(ind)<=0 or int(ind)>len(results[choice]['number']):
        print('Please provide a valid serial number🥺')
        ind = input("Which of the number will you like to update : ")

    ind = int(ind)-1
    new_number = input('Enter the new number : ')
    while not new_number.isnumeric():
        print('Please provide a number🥺')
        new_number = input('Enter the new number : ')

    contact_ind = all_contacts.index(results[choice])
    all_contacts[contact_ind]['number'][ind] = int(new_number)

    all_contacts_string = helper.convert_contacts_to_string(all_contacts)
    open('contacts.txt', 'w').write(all_contacts_string)
    print('Contact Updated👍🏼')

def add_another_number():
    name = input('Enter the name : ')
    all_contacts = helper.get_all_contacts(open('contacts.txt', 'r').read())
    results = helper.filter(all_contacts, name)

    if not results:
        print('\nNo contacts with given name found😐')
        return
    
    if len(results) == 1:
        new_number = int(input('Enter another number : '))

        contact_ind = all_contacts.index(results[0])
        all_contacts[contact_ind]['number'].append(new_number)
        
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
    
    new_number = int(input('Enter another number : '))

    contact_ind = all_contacts.index(results[int(choice)-1])
    all_contacts[contact_ind]['number'].append(new_number)
    
    all_contacts_string = helper.convert_contacts_to_string(all_contacts)
    open('contacts.txt', 'w').write(all_contacts_string)
    print('Contact Updated👍🏼')
    return
    

while running:
    print("""
1. Create a new contact
2. View all contacts
3. Find a contact
4. Delete a contact
5. Modify a name
6. Modify a number
7. Add another number of existing user
8. Exit
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
            add_another_number()

        elif choice == 8:
            running = False

        else:
            print("Invalid Choice")

    except:
        print('Wrong Input! Try again💥💥')
        print('')
        continue
    print('')
