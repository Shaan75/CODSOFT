names=[]
phn_nos=[]
emails=[]
addresses=[]
n=int(input("enter the capacity: "))
for i in range(n):
    name=input("Name: ")
    phn_no=int(input("PHONE NO.: "))
    email=input("email: ")
    address=input("address: ")

    names.append(name)
    phn_nos.append(phn_no)
    emails.append(email)
    addresses.append(address)
print("\nNAME\t\t\tPHN NO.\t\t\tEMAIL\t\t\tADDRESS\n")
for i in range(n):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i],phn_nos[i],emails[i],addresses[i]))
print("1. SEARCH")
print("2. DELETE")
print("3. ADD MORE")
print("4. EXIT")

while (n>0):
    x=int(input("Enter your choice no.: "))
    if (x==1):
        search_term= input("\nEnter search term: ")
        if search_term in names:
            index = names.index(search_term)
            phn_no= phn_nos[index]
            email= emails[index]
            address= addresses[index]
            print("NAME: {} PHONE NO: {}  EMAIL: {}  ADDRESS: {}".format(search_term, phn_no, email, address))
    elif (x==2):
        del_pos= int(input("Delete position: "))
        names.pop(del_pos)
        phn_nos.pop(del_pos)
        emails.pop(del_pos)
        addresses.pop(del_pos)
        print("After DELETE:\n")
        for i in range(n-1):
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i],phn_nos[i],emails[i],addresses[i]))
    elif (x==3):
        print("ENTER NEW CONTACT DETAILS:\n")
        name1=input("Name: ")
        phn_no1=int(input("PHONE NO.: "))
        email1=input("email: ")
        address1=input("address: ")

        names.append(name1)
        phn_nos.append(phn_no1)
        emails.append(email1)
        addresses.append(address1)
        for i in range(n+1):
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i],phn_nos[i],emails[i],addresses[i]))
    else:
        break
print("have a good day")
    

        
