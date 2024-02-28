
# OPENING A FILE

# Open a file with defalt read mode
file = open('001_top-5.txt')
print(file)

# Open the file as readable text
file = open('001_top-5.txt', 'rt')
# Read a whole file as one string
print(file.read())


# Open the file again because we already read until the end of the file previously.
# If we will not read it again, it will just return an empty list.
file = open('001_top-5.txt', 'rt')
# Read the whole file per line and convert to list per line
print(file.readlines())

# Another way of reading it back again from the top
file.seek(0)
# This will go back to the first line instead of reading it all again by using open

for line in file:
    print(line.strip())

# Close the file in the background.
file.close()

# WRITING IN A FILE

# Mode is 'w' to denote writing/overwriting the file
# We can change it to 'a' if we just want to append something on the file
file2 = open('001_test.txt', 'w')

file2.write('test line')

print(file2.name)
print(file2.closed)
print(file2.mode)

# Close in background
file2.close()


with open('001_top-5.txt') as file3:
    for line in file3:
        print(line.strip())
