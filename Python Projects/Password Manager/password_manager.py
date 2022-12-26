from cryptography.fernet import Fernet
import os
from tkinter import messagebox

psw = input("What is the master password? ")

if psw != "Sussybaka123":
    print("The password is incorrect.")
    exit()

path = f"{os.path.realpath(os.path.dirname(__file__))}/key.key"
if os.path.isfile(path) and os.access(path, os.R_OK):
    file = open(path, "rb")
    key = file.read()
    file.close
else:
    key = Fernet.generate_key()
    with open(path, "wb") as key_file:
        key_file.write(key)

fer = Fernet(key)

def add_input():
    website = input("What is the website/program? ")
    username = input("What is the username/email for " + website + "? ")
    password = input("What is the password for " + website + "? ")
    confirm = input("Are you sure you want to save this password? (Y/N) ")
    if confirm.lower() == "y":
        print("Saving the password to 'passwords.txt'...")
        path = f"{os.path.realpath(os.path.dirname(__file__))}/passwords.txt"
        with open(path, "a") as file:
            file.write(website + "|" + username + "|" + str(fer.encrypt(password.encode()).decode()) + "\n")
        print("The password was saved successfully.")
        messagebox.showinfo('Success', 'The password was saved successfully.')
        pass
    else:
        pass

def view():
    path = f"{os.path.realpath(os.path.dirname(__file__))}/passwords.txt"
    with open(path, "r") as read:
        for line in read.readlines():
            data = line.rstrip()
            website, user, password = data.split("|")
            print("Website: " + website + " | Username: " + user + " | Password: " + fer.decrypt(password).decode())
    pass

while True:
    print("")
    mode = input("Choose an action: (ADD/VIEW/EXIT) ").lower()
    if mode == "add":
        add_input()
    elif mode == "view":
        view()
    elif mode == "exit":
        print("Exiting the program...")
        exit()
    else:
        print("Invalid selection.")
        continue
