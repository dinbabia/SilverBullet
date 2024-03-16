"""
Debugger:
    next - we'll continue execution until the next line and stays within the current function
    step - execute the current line and will stop in a foreign function if one is called.

When you run this file using the basic python command, it will show the below.

(Pdb)
- Can create new variables
- Update/Delete variables...etc2
- Like running a python terminal
Commands:
    p <variable name> - print out the value of the variable name... we can also use 'print()'
    n - 'Next' from the description above
    s - 'Step' from the description above

Alternatively, we can call the module pdb when running a file.

python -m pdb <python_file>
"""

sample = "test"
print(sample)

breakpoint()
