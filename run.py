#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random

def create_user(user_name):
    '''
    Function to create a new user
    '''
    new_user = User(user_name)
    return new_user
def create_credential(password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(password)
    return new_credential

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def display_user():
    '''
    Function that returns all the saved user
    '''
    return User.display_user()
def display_credential():
    '''
    Function that returns all the saved user
    '''
    return Credential.display_credential()

def main():
    print("Hello, Welcome to your password-locker app. Please sign up and login")
    print('\n')

    while True:
        print("Username...")
        u_name = input()

        print("Password...")
        p_word = input()

        print('\n')
        print("Login now")

        print('\n')
        print("Username")
        U_name = input()

        print("Password")
        P_word = input()

        if U_name!=u_name and P_word != p_word:#error handling
            print("Wrong username or password. Reload page.")
            print('\n')
            break
        else:
            print(f"{U_name}...{P_word}") 
            print('\n')
            

    while True:
        print("Use these short codes:np- new password, gp-get password from us, del - delete password, dup-display passwords and accounts, ex-exit")
        short_codes=input().lower()

        if short_codes == 'np':
            print("New Password")
            print("-"*7)

            print("Account...")
            user_name = input()

            print("Password")
            password = input()

            save_users(create_user(user_name))
            save_credential(create_credential(password))
            print('\n')
            print(f"New Password {password} for {user_name} crated")
            print('\n')
        

        elif short_codes == 'gp':
            print("Get Password")
            print("-"*7)

            print("Account...")
            user_name = input()

            print("Password")
            random_number= random.randint(0,5)
            password = random_number, random_number, random_number, random_number

            save_users(create_user(user_name))
            save_credential(create_credential(password))
            print('\n')
            print(f"Password {password} for {user_name} created")
            print('\n')

        elif short_codes == 'dup':
            if display_user():
                print("Here is a list of all your account and their passwords")
                print('\n')

                for user in display_user():
                    print(f"{user.user_name}")
                    print('/n')
                for credential in display_credential():
                    print(f"{credential.password}")
                    print('/n')

            else:
                print('\n')
                print("You don't seem to have any contacts")
                print('\n')

        elif short_codes =='ex':
            print("Bye...")
            break

        else:
            print("Please use the short codes.")
    

if __name__ == '__main__':

    main()


