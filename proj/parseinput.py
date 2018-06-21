import argparse
parser = argparse.ArgumentParser()
parser.add_argument('echo')
parser.add_argument('-x')
args = parser.parse_args()
print dir(args)
print args.x
print args.echo

