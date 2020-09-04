#!/usr/bin/env python3.8

from random import choice,randint
from user import User
"""import the user class blueprint"""

from credentials import Credentials
"""import the credentials class blueprint"""

def create_credentials(accountName,username,password):
    '''
    Function to create a new user
    '''
    new_credentials = Credentials(accountName,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    Credentials.save_credential()

def del_credentials(contact):
    '''
    Function to delete a credential
    '''
    Credentials.credentials_list.remove()

def find_contact(number):
    '''
    Function that searches an acount by account_name and returns the credentials
    '''
    return find_by_name(accountName)

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
        special_chars=['!','?','_']
        password=''
        chars=['a','b','c']
        for _ in range(num_chars):
                password+=choice(chars)

        for _ in range(num_numbers):
                password+=str(randint(0,9))

        for _ in range(num_special):
                password+=choice(special_chars)

        print(f"{password}")
    




def main():
    print("Hello Welcome to Password Locker. What is your name?")
    name=input()
    print(f"Hello {name}. what would you like to do?")

    while True:
        print("USE THESE SHORT CODES :\ncc - create new credentials, \ndc - display all credentials, \ndel-delete account credentials, \nex -exit the password locker ")

        short_code = input().lower()

        if short_code == 'cc':
            print("Add new Credentials")
            print("-"*10)

            print ("Account name ....")
            account = input()

            print("Username ...")
            username = input()

            print("Password ...")
            password = input()


            save_credentials(create_credentials(account,username,password)) # create and save new account credentials.
            print ('\n')
            print(f"New account credentials {account} {username} created")
            print ('\n')

        elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your accounts credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.accountName} {credential.username} {credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You haven't saved any account details")
                                    print('\n')

        elif short_code == 'del':
            gen_password()

            """print("Enter the account name you want to remove")

                            del_number = input()
                      

                                    print("That account does not exist")"""

        elif short_code == "ex":
            print("Goodbye .......courtesy PLocker(vector) 2020")
            break
        
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
                """main function to run the module"""
main()