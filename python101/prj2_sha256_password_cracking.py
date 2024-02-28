from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid argument!")
    print(f">>> {sys.argv[0]} <sha256>")
    exit()

wanted_hash = sys.argv[1]
print(wanted_hash)

password_file = "ssh-common-passwords.txt"
attempts = 0

with log.progress(f"Attempting to back: {wanted_hash}!") as p:
    with open(password_file, "r", encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password)
            p.status(f"[{attempts}] {password.decode('latin-1')} == {password_hash}")
            if password_hash == wanted_hash:
                p.success(f"Password hash found after {attempts} attempts! {password.decode('latin-1')} hashes to {password_hash}!")
                exit()
            attempts += 1
        p.failure("Password hash not found!")
# Make sample sha
# >>> echo -ne <word> | sha256
