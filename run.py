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
    