def task():
    tasks = []
    print("-----TO DO LIST------")
    n=int(input("ENTER TOTAL NO. OF TASKS: "))
    for i in range(1,n+1):
        x=input(f"ENTER TASK {i} = ")
        tasks.append(x)
    print("Today's tasks are",tasks,"\n")
    while True:
        o= int(input("Enter 1-ADD\n2-UPDATE\n3-DELETE\n4-VIEW\n5-EXIT/STOP\n-> "))
        if o==1:
            add= input("ENTER TASK: ")
            tasks.append(add)
            print("TASK {add} has been successfully added")
        elif o==2:
            upd= input("ENTER UPDATABLE TASK")
            if upd in tasks:
                up=input("enter new task")
                ind= tasks.index(upd)
                tasks[ind]= up
                print("updated task",up)
        elif o==3:
            dlt= input("enter deletable task")
            if dlt in tasks:
                ind = tasks.index(dlt)
                del tasks[ind]
                print("TASK",dlt," has been deleted")
        elif o==4:
            print("total tasks = ",tasks)
        elif o==5:
            print("closing the programme....")
            break
        else:
            print("INVALID INPUT")
task()
            
                
                
            
            
               
