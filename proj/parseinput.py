import argparse
# enabling the argparser
parser = argparse.ArgumentParser()

# positional arguments
parser.add_argument("testsuite", help='some help text', default=None)
parser.add_argument("no_of_tc", type=int)
args = parser.parse_args()
print "testsuite:", args.testsuite
print "no_of_tc", args.no_of_tc, type(args.no_of_tc)

# parser = argparse.ArgumentParser()
# parser.add_argument('-x', type=float,
#                     help='first argument', )
# parser.add_argument('-y', type=float,
#                     help='second argument')
# args = parser.parse_args()
#
# print args
# print args.x, args.y
# #
# # parser.add_argument('echo')
# # parser.add_argument('-x')
# # args = parser.parse_args()
# # print dir(args)
# # print args.x
# # print args.echo
# #
