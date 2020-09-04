#!/usr/bin/env python3.8
from user import User
"""import the user class blueprint"""
from credentials import Credentials
"""import the credentials class blueprint"""

def create_credentials(account,username,password):
    '''
    Function to create a new user
    '''
    new_credentials = Credentials(account,username,password)
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

