from Functions import *

contacts = []

q = displaymenu()
contacts = readfile()

while q != 0 :
    # Add Contact
    if q == 1:
        print("================ Enter a Contact =================")
        name = input("Enter Name: ")
        mobile = input("Enter mobile: ")
        #contact=[name,mobile]
        contacts.append([name,mobile])
    # List Contacts
    elif q == 2:
        print("""=============== list of Contacts =================

        id ---------- name --------- mobile """)
        for i in range(len(contacts)):
            print("        ",i,"----------",contacts[i][0],"----------",contacts[i][1])
        print("""
==================================================""")
    # Search by name
    elif q == 3:
        print("=============== Search by Name ===================")
        name = input("Enter Name for search: ")
        for i in range(len(contacts)):
            if contacts[i][0] == name:
                print("mobile ",contacts[i][0]," is ",contacts[i][1])
                break    
    # Search by mobile
    elif q == 4:
        print("=============== Search by Mobile =================")
        mobile = int(input("Enter Mobile for search: "))
        for i in range(len(contacts)):
            if contacts[i][1] == mobile:
                print("mobile ",contacts[i][0]," is ",contacts[i][1])
                break  

    q = displaymenu()

if q==0:
    savefile(contacts)
        