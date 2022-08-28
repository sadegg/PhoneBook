
def displaymenu():
    menu = """
==================================================

=>      1: Add
=>      2: List
=>      3: search by name
=>      4: search by mobile
=>      0: exit

==================================================
"""
    print(menu)
    q = int(input("Choise a number: "))
    return q


#def readfile():
#    contacts=[]
#    f = open("Contacts.txt","r")
#    try:
#        for line in f:
#            contact= line[:-1].split(',')
#            contacts.append(contact)
#    finally:
#        f.close()
#        return contacts

def readfile():
    contacts=[]
    with open("Contacts.txt","r") as f:
        for line in f:
            contact= line[:-1].split(',')
            contacts.append(contact)
    return contacts


def savefile(contacts):
    f=open("Contacts.txt","w")
    try:
        for contact in contacts:
            f.write(contact[0]+',')
            f.write(contact[1]+'\n')
    finally:
        f.close()

    
    


