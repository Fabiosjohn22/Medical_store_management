import mysql.connector #importing module
print('''
_______________________________________
Welcome to the Shop Management Program
               -by Fabio Shivraj Joyce
_______________________________________''') #for GUI

mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin')
mycursor=mydb.cursor()

mycursor.execute('create database if not exists Sales_fsj')
mycursor.execute('use sales_fsj')

#for Login Table
mycursor.execute('create table if not exists login(username varchar(25) not null,password varchar(25) not null);')

#for purchase Table
mycursor.execute('create table if not exists purchase(date date not null,name varchar(25) not null,item_code int not null);')

#for stock
mycursor.execute('create table if not exists stock(item_code int not null primary key,item_name varchar(25) not null,quantity int not null,price int not null);')

#to save all the changes
mydb.commit()

z=0 #z=0 for empty set and z=1 for some entry in set
mycursor.execute('select * from login')
for i in mycursor:
    z+=1

if z==0:
    mycursor.execute("insert into login values('username','admin');")
    mydb.commit()

while True:
    print('''
    1. Store Admin
    2. Customer
    3. Exit Program
    _________________''') #for GUI Option selection
    ch=int(input('Enter your Choice: '))

    #if the user is an admin
    if ch==1:
        passwd=input('Enter the Password: ')
        mycursor.execute('select * from login')
        for i in mycursor:
            username,password=i

        if(passwd==password):
            print('''Successfully Logged in 🥳''')
            print('''________________________________''')
            #Options if Successfully Logged in
            print('''
            1. Add new item
            2. Update Price
            3. Delete Item
            4. Display all item
            5. To change the Password
            6. Log out
            ____________________________''')
            choice=int(input('Enter your Choice: '))

            #defining purpose of each options of Successful Login
            #add product
            if choice==1:
                loop='y'
                while loop=='y' or loop=='Y':
                    #get product data from admin
                    item_code=int(input('Enter the Product Code: '))
                    item_name=input('Enter the Product Name: ')
                    quantity=int(input('Enter quantity of Products to be added: '))
                    price=int(input('Enter the amount of individual product: '))
                    mycursor.execute("insert into stock values('"+str(item_code)+"','"+str(item_name)+"','"+str(quantity)+"','"+str(price)+"')")
                    mydb.commit()
                    print('''Stock added Successfully 😀''')
                    print('''
                    __________________________________''')
                    loop=input('Do you want to insert more items? (y/n): ')
                loop2=input('Do you want to continue editing stock? (y/n): ')

            #update product price
            elif choice==2:
                loop='y'
                while loop=='y' or loop=='Y':
                    item_code=int(input('Enter Product Code: '))
                    new_price=int(input('Enter the New Price: '))
                    mycursor.execute("update stock set price='"+str(new_price)+"'where item_code='"+str(item_code)+"'")
                    mydb.commit()
                    print('''Product's Price updated Successfully 😀''')
                    print('''
                    __________________________________''')
                    loop=input('Do you want to update price of more items? (y/n): ')
                loop2=input('Do you want to continue editing stock? (y/n): ')

            #delete product
            elif choice==3:
                loop='y'
                while loop=='y' or loop=='Y':
                    del_item_code=int(input('Enter the Product code to delete Product: '))
                    mycursor.execute("delete from stock where item_code='"+str(del_item_code)+"'")
                    mydb.commit()
                    print('''Product Successfully deleted 😀''')
                    loop=input('Do you want to delete more Products? (y/n): ')    
                loop2=input('Do you want to continue editing stock? (y/n): ')

            #show all products
            elif choice==4:
                mycursor.execute('select * from stock')
                print('item_code || item_name || item_quantity || indi_item_price')
                for i in mycursor:
                    t_code,t_name,t_quan,t_price=i
                    print(f"{t_code}    ||   {t_name}     ||     {t_quan}     ||     ₹{t_price}")

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

            #log out
            elif choice==6:
                break

        #Message when Unsuccessful Login
        else:
            print('''Wrong Password 😔''')

    #if the user is a customer
    elif ch==2:
        print('''
        1. Item Bucket
        2. Payment
        3. View Available Item
        4. Go Back
        ___________________________''')
        choice=int(input('Enter your choice: '))

        loop2='y'
        while loop2=='y' or loop2=='Y':
            print('''________________________________''')
            #Options when stayed in editing spot
            print('''
            1. Add new item
            2. Update Price
            3. Delete Item
            4. Display all item
            5. To change the Password
            6. Log out
            ____________________________''')
            ch=int(input('Enter your Choice: '))