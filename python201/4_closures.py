"""
Closures
- method of attaching data to code
- function object that remembers values in enclosing scopes,
even when that variable goes out of scope or even if it's removed.

- usefule when a nested function needs to reference a value in the outer scope
examples:
    1. if we wanna avoid global variables and instead use callbacks, or if we
    only have a few methods we want to implement in a Python class, then we can use this.

- When using these closures, we need to make sure to have a nested function which
refers to a value in the outer function,.. and that outer function returns the nested function.
"""

def print_out(a):
    print(f"Outer: {a}")

    def print_in():
        # This inner function will save the variable 'a' if the outer function 'print_out'
        # is assigned to a variable, hence, its return is this inner function.
        print(f"\tInner: {a}")

    return print_in

# Call the outer function, while assigning the inner function which is
# carrying/storing the variable 'a' to a variable.
# The data 'a' is now attached to the code/variable 'closure_1'
closure_1 = print_out("test")
print("Print Out not yet deleted")

del print_out

print("Print Out Deleted!")
# Call the inner function here
closure_1()

