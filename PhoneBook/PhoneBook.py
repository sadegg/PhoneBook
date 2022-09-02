from Functions import *

contacts = readfile()

while True :
    q = displaymenu()
    #exit
    if q == 0:
        savefile(contacts)
        break
    # Add Contact
    elif q == 1:
        contacts = add(contacts)
    # List Contacts
    elif q == 2:
       showList(contacts)
    # Search by name
    elif q == 3:
        search_by_name(contacts)
    # Search by mobile
    elif q == 4:
       search_by_mobile(contacts)
    elif q == 5:
        edit(contacts)
    elif q==6:
        delete(contacts)

