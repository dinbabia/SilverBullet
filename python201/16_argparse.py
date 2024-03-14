"""
- enables us to write command line interfaces/cli flexibly with python
- defines what arguments are required and we'll figure out how to pass data entered on the command line
during execution whether to actually perform exection or to complain that required parameters are missing or incorrect.

eg.
python 16_argparse.py
python 16_argparse.py -h
python 16_argparse.py din 10
python 16_argparse.py din 10 -bh
"""

import argparse

parser = argparse.ArgumentParser(description="Example CLI...")

# Positional Arguments. Required
parser.add_argument("hacker_name", help="Enter hacker name", type=str)
parser.add_argument("hacker_power", help="Enter hacker power", type=int)

# Optional Arguments. Not Required unless specified.
parser.add_argument("-bh", "--blackhat", default=False, action="store_true")

parser.add_argument("-hy", "--hackertype", choices=["whitehat", "blackhat"])

# We still need to parse the actual arguments
args = parser.parse_args()

print(args)

print(args.hacker_name)
print(args.hacker_power)
