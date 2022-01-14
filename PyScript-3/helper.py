#used to find the location where a new contact has to be added
def nearest_binary_search(li, value):
    if not li: return 0
    if value < li[0]: return 0
    if value > li[len(li)-1]: return len(li)
    l, r, n, mid = 0, len(li)-1, len(li), 0

    while r >= l:
        mid = (l+r)//2
        
        if li[mid] == value:
            return mid
        elif li[mid] < value:
            if mid < n-1 and li[mid+1] > value:
                return mid+1
            l = mid + 1
        else:
            if mid > 0 and li[mid-1] < value:
                return mid
            r = mid - 1
    return mid+1

#returns the string equivalent of all contacts as list of dictionary
def convert_contacts_to_string(contacts):
    res = ''
    for contact in contacts:
        res += f"{contact['name']},{contact['number']};"
    return res
    
#returns the contacts as list of dictionary after inserting given contact
def insert_contact(contacts, contact):
    list_of_names = [c['name'].lower() for c in contacts]
    contacts.insert(nearest_binary_search(list_of_names, contact['name'].lower()), contact)
    return contacts

#returns the list of dictionary of contacts after reading from the file
def get_all_contacts(contacts_read):
    return [{'name':x.split(',')[0].lstrip().rstrip(), 'number': int(x.split(',')[1])} for x in contacts_read.split(';')[:-1]]

#prints all the contacts there are present in the file
def display(contacts):
    ctr = 1
    for contact in contacts:
        print(f'\t{ctr}.\t',contact['name'], end="\t")
        if len(contact['name']) < 7:
            print('\t', end="")
        if len(contact['name']) < 15:
            print('\t', end='')
        print(contact['number'])
        ctr += 1

# returns all the contacts having a given substring present in them
def filter(contacts, value):
    result = []
    for contact in contacts:
        if contact['name'].lower().find(value.lower()) != -1:
            result.append(contact)
    return result

def delete_contact(contact_read, value, contact_write):
    to_be_deleated = filter(contacts_read, value)
    print(to_be_deleated)
    if len(to_be_deleated) > 1:
        while True:
            try:
                choice = int(input("Which one do you want to delete : "))
            except:
                print('Invalid Input, try again')
                continue
            if choice >= 1 and choice <= len(to_be_deleated):
                break
            else:
                print('Invalid Input, Try again')

    all_contacts = get_all_contacts(contacts_read)
    
    try:
        all_contacts.remove(to_be_deleated[choice-1])
    except:
        print("Some error occured while deleating💥")
    
    contact_write.write(convert_contacts_to_string(all_contacts))

def write(contact_write, contacts_as_string):
    contact_write.write(contacts_as_string)
