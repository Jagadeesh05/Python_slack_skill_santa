database={
    "Nikhil1123":{
        'Name':"Nikhil Ambigar",
        'Age' : 20,
        'Email': "ambigarnikhil@gmail.com",
        'Password': "ruby@1123",
        'Amount': 250000,
        },
    "Prajwal2256":{
        'Name':"Prajwal Bhosle",
        'Age' : 20,
        'Email': "prajwalbhosle@gmail.com",
        'Password': "rohi@1123",
        'Amount': 250000,
        }
    }
import sys
while(1>0):
    print("Welcome to JOKER'S Bank")
    print("1. Sign in ")
    print("2. Sign up ")
    print("3. Exit ")  
    a=input("Enter your choice:")
    if(a=="1"):
        username=input("Enter the username:")
        Password=input("enter the password:")
        if(database.get(username)):
            print("Welcome",database[username]["Name"])
            print("1. Check balance")
            print("2. Deposit balance")
            print("3. Withdrawl")
            print("4. Logout")
            b=input("Enter your choice:")
            if(b=="1"):
               print("Current Balance :",database[username]['Amount'])
            elif(b=="2"):
                amount=int(input("Enter the amount to add in your account:"))
                database[username]['Amount']=database[username]['Amount']+amount
                print("Current Balance :",database[username]['Amount'])
            elif(b=="3"):
                amount=int(input("Enter the amount for withdrawl:"))
                database[username]['Amount']=database[username]['Amount']-amount
                print("Current Balance :",database[username]['Amount'])
            elif(b=="4"):
                username="Null"
                print("Logging out...........")
                print("Logged out")
            else :
                print("Invalid choice, Please enter approriate choice")
        else:
            print("Username Not Found")
    elif(a=='2'):
        print("Enter the following details for Sign up")
        username_1=input("Enter the Username:")
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        password=input("Enter your password:")
        email=input("Enter the email:")
        balance=int(input("Enter balance in your account:"))
        database[username_1]={}
        database[username_1]['Name']=name
        database[username_1]['Age']=age
        database[username_1]['Email']=email
        database[username_1]['Password']=password
        database[username_1]['Amount']=balance
        print("Username successfully created")
    elif(a=='3'):
        sys.exit()
    else:
        print("Enter the valid option")
        
                
                
                
                
                
                
                
                
                
                
                
