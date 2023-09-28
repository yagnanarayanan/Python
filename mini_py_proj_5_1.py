# password manager
import datetime
from cryptography.fernet import Fernet

# run below function only once to create the key file
# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)


# write_key()
def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    service = input("Enter the service: ")
    with open("acct_codes.txt", 'r') as f:
        for line in f.readlines():
            if line.rstrip("\n").rsplit("|")[0] == service:
                print(f"Service     : {line.rstrip().rsplit('|')[0]}")
                print(f"Account Name: {line.rstrip().rsplit('|')[1]}")
                # print(f"Password    : {line.rstrip().rsplit('|')[2]}")
                password = line.rstrip().rsplit('|')[2]
                print(f"Password    : {fer.decrypt(password.encode()).decode()}")
                print(f"Load date   : {line.rstrip().rsplit('|')[3]}")
                break
        else:
            print(f"The service {service} does not exist in file.")


def add():
    service = input("Enter the name of the service: ")
    account_name = input("Enter account name: ")
    pwd = input("Enter password: ")
    load_dtm = datetime.datetime.now()
    with open("acct_codes.txt", 'a') as f:
        f.write(service + "|" + account_name + "|" + fer.encrypt(pwd.encode()).decode() + "|" + str(load_dtm) + "\n")


while True:
    mode = input("Do you want to add a new password or view a password (view, add) ?. Press q to quit. ").lower()
    if mode == "q":
        print("Quitting...")
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid input, please try again.")
        continue
