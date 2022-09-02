def displaymenu():
    menu = """
==================================================

=>      1: Add
=>      2: List
=>      3: search by name
=>      4: search by mobile
=>      5: edit
=>      6: delete
=>      0: exit

==================================================
"""
    print(menu)
    q = int(input("Choise a number: "))
    return q

def readfile():
    contacts = []
    with open("Contacts.csv","r") as f:
        for line in f:
            contact = line[:-1].split(',')
            contacts.append(contact)
    return contacts

def savefile(contacts):
   with open("Contacts.csv","w") as f:
        for contact in contacts:
            f.write(contact[0] + ',')
            f.write(contact[1] + '\n')   

def add(contacts):
    print("================ Enter a Contact =================")
    name = input("Enter Name: ")
    mobile = input("Enter mobile: ")
    #contact=[name,mobile]
    contacts.append([name,mobile])
    savefile(contacts)
    return contacts

def showList(contacts):
     print("=============== list of Contacts =================")
     print("         ID----------",contacts[0][0],"----------",contacts[0][1])
     for i in range(1,len(contacts)):
        print("        ",i,"----------",contacts[i][0],"----------",contacts[i][1])
     print("==================================================")

def search_by_name(contacts):
    print("=============== Search by Name ===================")
    name = input("Enter Name for search: ")
    for i in range(len(contacts)):
        if contacts[i][0] == name:
            print("mobile ",contacts[i][0]," is ",contacts[i][1])
            break    

def search_by_mobile(contacts):
    print("=============== Search by Mobile =================")
    mobile = input("Enter Mobile for search: ")
    for i in range(len(contacts)):
        if contacts[i][1] == mobile:
            print("mobile ",contacts[i][0]," is ",contacts[i][1])
            break  

def edit(contacts):
    showList(contacts)
    id = int(input("Choose an ID from the list above: "))
    name = input("Enter New Name (if not change press Enter): ")
    mobile = input("Enter New Mobile (if not change press Enter): ")
    if name != '':
        contacts[id][0] = name
    if mobile != '':
        contacts[id][1] = mobile
    savefile(contacts)
    print("Edit successful")
   
def delete(contacts):
    df=pd.read_csv('Contacts.csv')
    showList(contacts)
    id = int(input("Choose an ID from the list above: "))
    r = input("Are you sure to delete " + contacts[id][0]+" (y OR n)? ")
    if r == 'y':
        del contacts[id]
    savefile(contacts)
    print("Delete successful")