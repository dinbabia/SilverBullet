import subprocess

# subprocess.call(["calc"], shell=True)

# out = subprocess.check_call(["cmd", "/c", "calc"])

out = subprocess.check_output(["cmd", "/c", "whoami"])
print(out.decode())
