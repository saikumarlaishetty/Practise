# https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/

# Edit the program configurations at the right top corner and send some parameters to sum them up.

# Eg: python Argparse.py 1 2 3 4
# output : 10

import argparse

"""
Steps for Using Argparse
==============================

Step 1:

Creating a Parser: Importing argparse module is the first way of dealing with the concept. After you’ve imported it you have to create a parser or
an ArgumentParser object that will store all the necessary information that has to be passed from the python command-line.

Syntax:
Syntax: class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], 
formatter_class=argparse.HelpFormatter, prefix_chars=’-‘, fromfile_prefix_chars=None, argument_default=None, 
conflict_handler=’error’, add_help=True, allow_abbrev=True) 


"""

parser = argparse.ArgumentParser(description='Process some integers')


"""
Step 2:

Adding Arguments: Next step is to fill the ArgumentParser with the information about the arguments of the program. 
This implies a call to the add_argument() method. These information tell ArgumentParser how to take arguments from the
command-line and turn them into objects.

Syntax: ArgumentParser.add_argument(name or flags…[, action][, nargs][, const][, default][, type][, choices]
[, required][, help][, metavar][, dest])

"""

parser.add_argument('integers', metavar='N',
                    type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument(dest='accumulate',
                    action='store_const',
                    const=sum,
                    help='sum the integers')


""""
STEP 3:

Parsing Arguments: The information gathered in the step 2 is stored and used when arguments are parsed through parse_args(). 
The data is initially stored in sys.argv array in a string format. Calling parse_args() with the command-line data first 
converts them into the required data type and then invokes the appropriate action to produce a result.

Syntax: ArgumentParser.parse_args(args=None, namespace=None)

"""

args = parser.parse_args()
print(args.accumulate(args.integers))

