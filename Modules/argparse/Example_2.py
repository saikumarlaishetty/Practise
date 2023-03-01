import argparse

# Initializing Parser
parser = argparse.ArgumentParser(description="sort some integers")

# Adding argument
parser.add_argument('integers',
                    metavar='N',
                    type=int,
                    nargs = '+',
                    help = 'an integer for the accumulator')

parser.add_argument(dest='accumulate',
                    action='store_const',
                    const=sorted,
                    help='arranges the integers in ascending order')

args = parser.parse_args()
# print(args.accumulate(args.integers))
print(dir(args))