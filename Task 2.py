print("~~~~~~~~~~~Mini Calculator~~~~~~~~~~~")
while True:
    n1= float(input("Enter number :"))
    n2= float(input("Enter another number :"))
    print("1. Addition\n")
    print("2. Substraction\n")
    print("3. Multiplication\n")
    print("4. Divvision\n")
    print("5. Exit\n")
    choice = int(input("your choice from 1-5: "))
    if choice==1:
        print("Addition= ",n1+n2)
    elif choice==2:
        print("Substraction= ",n1-n2)
    elif choice==3:
        print("Multiplication= ",n1*n2)
    elif choice==4:
        print("Division= ",n1/n2)
    elif choice==5:
        break
    else:
        print("INVALID INPUT")
