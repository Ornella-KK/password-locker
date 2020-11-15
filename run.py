#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(user):
    new_user = User(user_name)
    return new_user
def create_credential(credential):
    new_credential = Credential(password)
    return new_credential

def save_users(user):
    user.save_user()
def save_credential(credential):
    credential.save_credential()

def del_user(user):
    user.delete_user()
def del_credential(credential):
    credential.delete_credential()

def display_user():
    return User.display_user()
def display_credential():
    return Credential.display_credential()

def main():
    print("Hello, Welcome to your password-locker app. Please sign up and login")
    print('\n')

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
        print("Wrong username or password")
    else:
        print(f"{U_name}...{P_word}") 

        print('\n')
        print("Use these short codes:np- new password, del - delete password, dup-display passwords and accounts, ex-exit")
        short_codes=input().lower()

    


if __name__ == '__main__':

    main()


