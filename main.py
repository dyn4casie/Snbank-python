#libraries
import random
import os
import datetime

#bankAppMain = True
#Variables
username = ""
password = ""
full_name = ""
account_name = ""
account_number = ""
account_type = ""
account_email = ""
opening_balance = 0.00

#staff login function
def staff_login():
    user_exist= False
    username = input("Enter username here : ")
    password = input("Enter password here : ")
    staff = open("staff.txt", "r")
    check =staff.readlines()
    detail = username+":"+password
    for x in check :
        yes= detail in str(x)
        if yes == True:
           user_exist = True
    staff.close()
    if user_exist:
        print("Login successful\n###############################################\n")
        user_session = open("user_session.txt", "w")
        user_session.write(username+" logged in successfully at ")
        user_session.write(str(datetime.datetime.now())) # prints the current date and time in the file
        user_session.close()
    else:
        print ("User details does not exist")
    return user_exist,username

#function to generate account number
def generate_account_number():
    generate=True
    while generate:
        account_number = "2"+''.join(random.choice("0123456789")for i in range(9))
        customer = open("customer.txt", "r")
        check =customer.readlines()
        for x in check :
            yes= account_number in str(x)
            if yes == True:
                generate = True
            else:
                generate = False
    else:
        print ("Account number is ", account_number)
    

    return account_number

#function to create account
def create_account (username):
    account_name = input ("Enter account name : ")
    account_email = input ("Enter account email : ")
    correct_email = check_email(account_email)          #jump to the function check_email()
    while correct_email==False:
        print ("The email address you entered is INVALID! Please try again.")
        account_email = input("\nEnter email here: ")
        correct_email = check_email(account_email)
        
    print ("Select account type. \n1. Current \n2. Savings \n3. Business")
    _type = input(">>")
    if _type == "1":
        account_type = "Current"
    elif _type == "2":
        account_type = "Savings"
    elif _type == "3":
        account_type = "Business"
    opening_balance = input("Enter opening balance : ")
    account_number = generate_account_number()
    customers = open("customer.txt", "a")
    account_details = "\n"+account_name+" ; "+account_number+" ; "+account_type+ " ; "+ account_email+ " ; "+ str(opening_balance)
    customers.write(account_details)
    customers.write("\n   created by "+username+" at "+str(datetime.datetime.now()))
    print("Account created successfully")
    customers.close()

    user_session = open("user_session.txt", "a")
    user_session.write("\n   Created account "+account_number+" at ")
    user_session.write(str(datetime.datetime.now())) # prints the current time in the file
    user_session.close()
    

    return account_number

#This function checks the validity of the email supplied 
def check_email(email):
    
    com = email.endswith(".com") #This will check if the email ends with .com
    at = '@' in email            #this will check if the email contains the character @
    
    if com == True and at == True:
        correct_email=True
    else:
        correct_email=False
        
    return correct_email

#function to fetch account details
def fetch_account(account_number,username):
    customers = open("customer.txt", "r")
    fetching =customers.readlines()
    for x in fetching:
        yes = account_number in str(x)
        if  yes:
            print("Find account details below. \naccount_name ; account_number ; account_type ;  account_email ; opening_balance")
            print(x)

    user_session = open("user_session.txt", "a")
    user_session.write("\n"+username+" checked account details of "+account_number+" at ")
    user_session.write(str(datetime.datetime.now())) # prints the current time in the file
    user_session.close()

#main function
def main():
    print("<----------------------------->\nHello, Good day! \nWelcome to StartNg Bank Plc.")
    action = input("1. Staff Login \n2. Close App \n<----------------------------->\n")
    while action == "1":
        user_exist,username=staff_login()
        
        while user_exist==True:
            action=""
            print("<------------------------------------------>\nWhat would you like to do? Enter 1,2 or 3.")
            action = input("1. Create new Account. \n2. Check Account details. \n3. Log Out \n<------------------------------------------>\n")
            if action == "1":
                create_account(username)
            elif action == "2":
                account_number = input("Enter account number here: ")
                fetch_account(account_number,username)
            elif action == "3":
                os.remove("user_session.txt")
                user_exist = False
                main()
            else:
                print ("Invalid input! Please enter a valid input")

        else: 
            print("No User is logged in")
            main()


    else:
        if action == "2":
            exit()
        else: 
            print("Invalid input! Try again!")
            main()
main()