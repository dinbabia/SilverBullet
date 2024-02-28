import sys


print(sys.version)

# Executable binary
print(sys.executable)

# linux, windows, etc
print(sys.platform)

# Type any input in sys.stdin then writes out on stdout
for line in sys.stdin:
    if line.strip() == "exit":
        break
    sys.stdout.write(f">>> {line}")

import time

for i in range(1, 51):
    time.sleep(0.1)
    sys.stdout.write(f"{i:>2} [{'#'*i}{'.'*(50-i)}]\n")
    sys.stdout.flush()


# Returns a list. First item/index is the file name
# Proceeding items/indexes are from the arguments
# e.g. 
# >>> 003_sys.py din hello 123 test
# Which will result to
# ['003_sys.py', 'din', 'hello', '123', 'test']
print(sys.argv)

