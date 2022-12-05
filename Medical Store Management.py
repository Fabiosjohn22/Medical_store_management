import mysql.connector #importing module
print('''
_______________________________________________
Welcome to the Medical Shop Management Program
               -by Fabio Shivraj Joyce
_______________________________________________''') #for GUI

mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin')
mycursor=mydb.cursor()

mycursor.execute('create database if not exists Medicine_sales_fsj')
mycursor.execute('use Medicine_sales_fsj')

#for Login Table
mycursor.execute('create table if not exists login(username varchar(25) not null,password varchar(25) not null);')

#for purchase Table
mycursor.execute('create table if not exists purchase(date date not null,name varchar(25) not null,item_code int not null,amount int(11) not null);')

#for stock
mycursor.execute('create table if not exists stock(item_code int not null primary key,item_name varchar(25) not null,composition_in_mg varchar(100),quantity int not null,price int not null);')

#to save all the changes
mydb.commit()

z=0 #z=0 for empty set and z=1 for some entry in set
mycursor.execute('select * from login')
for i in mycursor:
    z+=1

if z==0:
    mycursor.execute("insert into login values('username','admin');")
    mydb.commit()

#Defalt Database
if z==0:
    mycursor.execute('insert into stock values(1,"Tivomac","Ivermectin 200 mg",200,250);')
    mycursor.execute('insert into stock values(2,"Limazole","Albendazole 500 mg",300,800);')
    mycursor.execute('insert into stock values(3,"Nurokind-Plus","Mecobalamin 45 mg",150,500);')
    mycursor.execute('insert into stock values(4,"Sulphas-Plus","Sulphadin 80 mg",200,600);')
    mycursor.execute('insert into stock values(5,"Pyrogesic","Piroxicam 90 mg",100,900);')
    mycursor.execute('insert into stock values(6,"Amitek","Amikasin Sulphate 250mg/ml",100,1075);')
    mycursor.execute('insert into stock values(7,"Butavon","Butaphosphon 100mg & Vitamin B1250mcg",300,570);')
    mycursor.execute('insert into stock values(8,"Cipkon-TZ","Ciprofloxacin 1500mg Tinidazole 1800mg",300,1440);')
    mycursor.execute('insert into stock values(9,"Flexicon","Enrofloxacin 1500mg",500,1400);')
    mydb.commit()

while True:
    print('''
    1. Medical Store Admin
    2. Customer
    3. Exit Program
    _________________''') #for GUI Option selection
    ch=int(input('Enter your Choice: '))

################### Admin Section ########################
    #if the user is an admin
    if ch==1:
        passwd=input('Enter the Password: ')
        mycursor.execute('select * from login')
        for i in mycursor:
            username,password=i

        loop2='y'
        while loop2=='y' or loop2=='Y':
            if(passwd==password):
                print('''Successfully Logged in 🥳''')
                print('''________________________________''')
                #Options if Successfully Logged in
                print('''
                1. Add new Medicine
                2. Update Price
                3. Delete Medicine
                4. Display all Medicines
                5. To change the Password
                6. Log Out
                ____________________________''')
                choice=int(input('Enter your Choice: '))

                #defining purpose of each options of Successful Login
                #add medicines
                if choice==1:
                    loop='y'
                    while loop=='y' or loop=='Y':
                        #get medicine data from admin
                        item_code=int(input('Enter the Medicine Code: '))
                        item_name=input('Enter the Medicine Name: ')
                        quantity=int(input('Enter quantity of Medicines to be added: '))
                        price=int(input('Enter the amount of an individual Medicine: '))
                        mycursor.execute("insert into stock values('"+str(item_code)+"','"+str(item_name)+"','"+str(quantity)+"','"+str(price)+"')")
                        mydb.commit()
                        print('''Stock added Successfully 😀''')
                        print('''
                        __________________________________''')
                        loop=input('Do you want to insert more Medicines? (y/n): ')
                    loop2=input('Do you want to continue editing stock? (y/n): ')

                #update Medicine price
                elif choice==2:
                    loop='y'
                    while loop=='y' or loop=='Y':
                        item_code=int(input('Enter Medicine Code: '))
                        new_price=int(input('Enter the New Price: '))
                        mycursor.execute("update stock set price='"+str(new_price)+"'where item_code='"+str(item_code)+"'")
                        mydb.commit()
                        print('''Medicine's Price updated Successfully 😀''')
                        print('''
                        __________________________________''')
                        loop=input('Do you want to update price of more Medicines? (y/n): ')
                    loop2=input('Do you want to continue editing stock? (y/n): ')

                #delete Medicine
                elif choice==3:
                    loop='y'
                    while loop=='y' or loop=='Y':
                        del_item_code=int(input('''Enter the Medicine's code to delete it: '''))
                        mycursor.execute("delete from stock where item_code='"+str(del_item_code)+"'")
                        mydb.commit()
                        print('''Medicine Successfully deleted 😀''')
                        loop=input('Do you want to delete more Medicines? (y/n): ')    
                    loop2=input('Do you want to continue editing stock? (y/n): ')

                #show all medicines
                elif choice==4:
                    mycursor.execute('select * from stock')
                    print('''Medicine's Code || Medicine's name || Medicine's Composition || Medicine's quantity || Medicine's price''')
                    for i in mycursor:
                        t_code,t_name,t_composition,t_quan,t_price=i
                        print(f"{t_code}    ||   {t_name}     ||   {t_composition}     ||     {t_quan}     ||     ₹{t_price}")

                #change password
                elif choice==5:
                    old_pass=input('Enter Old Password: ')
                    mycursor.execute('select * from login')
                    for i in mycursor:
                        username,password=i
                    if old_pass==password:
                        new_pass=input('Enter New Password: ')
                        new_pass_r=input("Repreat Password: ")
                        if new_pass==new_pass_r:
                            mycursor.execute("update login set password='"+new_pass+"'")
                            mydb.commit()
                            print('''Password Updated 🥳''')
                        else:
                            print('''⚠️⚠️⚠️ Passwords are not matching ☠️ ⚠️⚠️⚠️''')
                    else:
                        print('''Wrong Password 😔''')

                #back to user selection
                elif choice==6:
                    print("Logged out Successfully")
                    break

                else:
                    print('Option does not exists')
                    break
            
            #Message when Unsuccessful Login
            else:
                print('''
                Wrong Password 😔 
                Try Again
                ''')
                break


################### Customer Section ########################
    #if the user is a customer
    elif ch==2:
        print('''
        1. Medicine Bucket
        2. Payment Amount
        3. View Available Medicine
        4. Exit
        _____________________________''')
        C_choice=int(input('Enter your choice: '))
        if C_choice==1:
            C_name=input('Enter your Legal name: ')
            item_code=int(input('''Enter the Medicine's code of medicine you want to purchase: '''))
            quantity=int(input('Enter the quantity of Medicine to be purchased: '))
            mycursor.execute("select * from stock where item_code='"+str(item_code)+"'")

            for i in mycursor:
                t_code,t_name,t_composition,t_quan,t_price=i
                amount=t_price*quantity #amount to be paid
                net_quantity=t_quan-quantity #decreasing medicine quantity as a variable
                mycursor.execute("update stock set quantity='"+str(net_quantity)+"'where item_code='"+str(item_code)+"'") #decreasing the product quantity from stock
                mycursor.execute("insert into purchase values(now(),'"+C_name+"','"+str(item_code)+"','"+str(amount)+"')")
                print('''Successfully added the Medicine to your Medicine List''')
                mydb.commit()
                break
            break
        #for payment
        elif C_choice==2:
            mycursor.execute('select sum(amount) from purchase;')
            amount=mycursor.fetchall()
            amt=str(amount)
            total='₹'
            num=('1','2','3','4','5','6','7','8','9','0')
            for i in amt:
                if i in num:
                    total+=i
            print("""Your Medicines 💊 would cost: """,total)
            print('''
            _______________________________
            Thank You for Purchasing
                See you soon 😀
            _______________________________''')
            break

        #show all medicines
        elif C_choice==3:
            mycursor.execute('select * from stock')
            print('''Medicine's Code || Medicine's name || Medicine's Composition || Medicine's quantity || Medicine's price''')
            for i in mycursor:
                t_code,t_name,t_composition,t_quan,t_price=i
                print(f"{t_code}    ||   {t_name}     ||   {t_composition}     ||     {t_quan}     ||     ₹{t_price}")

        
        #to exit
        elif C_choice==4:
            break
        elif C_choice not in [1,2,3,4]:
          print('Option not available/nPlease try again.')
          C_choice=int(input('Enter your choice: '))
          if ch==2:
            print('''
            1. Medicine Bucket
            2. Payment Amount
            3. View Available Medicine
            4. Exit
            _____________________________''')
            C_choice=int(input('Enter your choice: '))
        if C_choice==1:
            C_name=input('Enter your Legal name: ')
            item_code=int(input('''Enter the Medicine's code of medicine you want to purchase: '''))
            quantity=int(input('Enter the quantity of Medicine to be purchased: '))
            mycursor.execute("select * from stock where item_code='"+str(item_code)+"'")

            for i in mycursor:
                t_code,t_name,t_composition,t_quan,t_price=i
                amount=t_price*quantity #amount to be paid
                net_quantity=t_quan-quantity #decreasing medicine quantity as a variable
                mycursor.execute("update stock set quantity='"+str(net_quantity)+"'where item_code='"+str(item_code)+"'") #decreasing the product quantity from stock
                mycursor.execute("insert into purchase values(now(),'"+C_name+"','"+str(item_code)+"','"+str(amount)+"')")
                print('''Successfully added the Medicine to your Medicine List''')
                mydb.commit()

        #for payment
        elif C_choice==2:
            mycursor.execute('select sum(amount) from purchase;')
            amount=mycursor.fetchall()
            amt=str(amount)
            total='₹'
            num=('1','2','3','4','5','6','7','8','9','0')
            for i in amt:
                if i in num:
                    total+=i
            print("""Your Medicines 💊 would cost: """,total)
            print('''
            _______________________________
            Thank You for Purchasing
                See you soon 😀
            _______________________________''')
            break

        #show all medicines
        elif C_choice==3:
            mycursor.execute('select * from stock')
            print('''Medicine's Code || Medicine's name || Medicine's Composition || Medicine's quantity || Medicine's price''')
            for i in mycursor:
                t_code,t_name,t_composition,t_quan,t_price=i
                print(f"{t_code}    ||   {t_name}     ||   {t_composition}     ||     {t_quan}     ||     ₹{t_price}")               
    
    elif ch==3:
        break
