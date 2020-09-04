#!/usr/bin/env python3.8
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
    save_credential()

def del_credentials(contact):
    '''
    Function to delete a credential
    '''
    delete_credential()

def find_contact(number):
    '''
    Function that searches an acount by account_name and returns the credentials
    '''
    return find_by_name(accountName)

def display_credentials():
    '''
    Function that returns all the saved account credentials
    '''
    return display_credential()

def copy_credentials():
    '''
    Function that copies account details to clipboard
    '''
    return copy_credentials()

def generate_password():
    '''
    Function that generates a password for an account
    '''
    return gen_password()


def main():
    print("Hello Welcome to Password Locker. What is your name?")
    
    name=input()
        print(f"Hello {name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create new credentials, dc - display all credentials, del-delete account credentials ex -exit the password locker ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("Add new Credentials")
                            print("-"*10)

                            print ("Account name ....")
                            f_name = input()

                            print("Username ...")
                            l_name = input()

                            print("Password ...")
                            p_number = input()


                            save_credentials(create_credentials(accountName,username,password)) # create and save new account credentials.
                            print ('\n')
                            print(f"New account credentials {accountName} {username} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your accounts credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.accountName} {credential.username}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You haven't saved any accounts details")
                                    print('\n')

                    elif short_code == 'del':

                            print("Enter the account name you want to remove")

                            del_number = input()
                      

                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Goodbye .......courtesy PLocker(vector) 2020")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

