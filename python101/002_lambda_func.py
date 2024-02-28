
# Break the string into lists of a given length
blocks = lambda x, y: [x[i:i+y] for i in range(0, len(x), y)]

print(blocks("Laurence", 3))

