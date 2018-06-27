import argparse
def square(x):
    print x * x

def add(x, y):
    print x + y
parser = argparse.ArgumentParser()
# parser.add_argument('userstring', help='Enter a string that you want to be converted to upper case')
# print "User passed", args.userstring
# print args.userstring.upper()
# parser.add_argument('x', type=int)
# args = parser.parse_args()
# square(args.x)

parser.add_argument('-x', type=int, default=0)
parser.add_argument('-y', type=int, default=0)
args = parser.parse_args()
add(args.x, args.y)
#square(args.x)