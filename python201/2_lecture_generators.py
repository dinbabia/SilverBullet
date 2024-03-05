'''
Generators
- Provide a simple way to create iterators
- returns iterable set of items one at a time
- define a normal function but give yield statement rathen than return statement

- the return statement, would terminate the function entirely
- the yield statement, pause the function and saving the state and local variable information,
so we can later continue from that point.

- very useful to use for memory intensive processing or reading of large files
because generators use lazy execution
- only produce items when they are asked for, rather than computing the entire sequence at once

'''

def generator_1():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

item_1 = generator_1()
# This will print a generator object
print(item_1)

# We need to use a function called 'next' to return the current local variable information that is yielded
# from its current state (it will reset once we execture the running time again)
# From our example, it will return 1
print(next(item_1))
# Next will be 2 (it will continue from its previous state)
print(next(item_1))
# StopIteration Error will occur when a generator function terminates
# If we use a loop, the loop knows when it reaches the StopIteration Error


def xor_static_key(a):
    """
    generator function
    static xor function with a key
    """
    key = 0x5
    # For each character in the string that was passed in
    for i in a:
        # yield the ord of that character, and xor with that key
        yield chr(ord(i) ^ key)

for i in xor_static_key("test"):
    print(f"xor: {i}")

xor_static_key_2 = (chr(ord(i) ^ 0x5) for i in "test")
print(xor_static_key_2)
print(next(xor_static_key_2))



