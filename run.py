#!/usr/bin/env python3.8

from random import choice,randint
from user import User
"""import the user class blueprint"""

from credentials import Credentials
"""import the credentials class blueprint"""

def create_user(username,password):
	'''
	Function to create a new user account
	'''
	new_user = User(username,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_login(user)

def confirm_user(username,password):
	'''
	Function that verifies the existance of the user before allowing login
	'''
	Credentials.confirmed(first_name,password)
	return confirmed

def create_credentials(accountName,username,password):
    '''
    Function to create new account credentials
    '''
    new_credentials = Credentials(accountName,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    Credentials.save_credential(credentials)
    

def del_credentials(account):
    '''
    Function to delete a credential
    '''
    Credentials.credentials_list.remove(account)


def display_credentials():
    '''
    Function that returns all the saved account credentials
    '''
    return Credentials.display_credential()

def copy_credentials():
    '''
    Function that copies account details to clipboard
    '''
    return copy_credentials()

def gen_password(num_chars=3,num_numbers=3, num_special=2):
        '''function to generate a random password'''
        special_chars=['!','?','_','*','@']
        password=''
        chars=['a','b','c','d','e','f','g']

        '''loop to iterate through the numbers, characters and special characters and return a random password'''
        for _ in range(num_chars):
                password+=choice(chars)

        for _ in range(num_numbers):
                password+=str(randint(0,9))

        for _ in range(num_special):
                password+=choice(special_chars)

        return password
    




"""Main execution program"""
def main():
    print("Hello! Welcome to PASSWORD LOCKER ")
    while True:
        print("USE THESE SHORT CODES :\nca-create account, \nli - login to your account, \nex -exit password locker ")

        short_code = input().lower() #get user input
        if short_code == 'ca':
            print('Create a new account')
            print('*'*10) #add decoration

            print("Username...")
            username= input() #get username from user

            print ('Password...')
            password= input() #get password from user

            save_user(create_user(username,password)) # create and save new user account.
            print(f"New User: {username} Password:{password}created successfully")

        elif short_code == 'li': #login option
            print("Enter your Username") #prompt for username
            username= input()

            print('Enter your Password') #prompt for password
            password= input()

            confirm_user(username,password)#check if user exists

            if Credentials.confirmed: #if user exists proceed
            
                """credential creation and manipulation functions"""
            
                print(f"Hello {username} Welcome to your Password Locker account.") 

                while True:
                    print("WHAT WOULD YOU LIKE TO DO? :\ncc - create new credentials, \ndc - display all credentials, \ndel-delete account credentials, \nex -exit the password locker ")
                    '''prompt for user input to proceed'''
                    short_code = input().lower()

                    if short_code == 'cc': 
                        print("Add new Credentials")
                        print("-"*10)

                        print ("Account name ....")
                        account = input()

                        print("Username ...")
                        username = input()

                        print("I WOULD LIKE TO \n cp - create my own password \n gp - generate a password :)")
                        short_code = input().lower()

                        if short_code== 'cp':
                            print ("Enter password")
                            password=input()

                        elif short_code== 'gp':
                            print ("This is yor password:")
                            gen_password()
                            print(f"{password}")


                        save_credentials(create_credentials(account,username,password)) # create and save new account credentials.
                        print ('\n')
                        print(f"New account credentials, NAME: {account}\n USER: {username}  added successfully")
                        print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your accounts credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.account} {credential.username} {credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You haven't saved any account details")
                                    print('\n')

                    elif short_code == 'del':
                        print("Enter the name of account you wish to delete:")
                        account=input()
                        del_credentials(account)

               
                    elif short_code == "ex": #exit  credential creation on user selection
                        print("Goodbye .......courtesy PLocker(vector) 2020")
                        break
        
                    else:
                        print("I really didn't get that. Please use the short codes")
            
            else: #if user does not match any inform user
                print("User does not exist or incorrect input!")


        elif short_code == "ex": #exit the program on user selection
            print("Goodbye .......courtesy PLocker(vector) 2020")
            break

        else:#if input not in short codes, inform user
            print("I really didn't get that. Please use the short codes")

    
if __name__ == '__main__':
                """main function to run the module"""
main()