import sys
def add(x,y):
    return x + y

print sys.argv
print add(int(sys.argv[1]), int(sys.argv[2]))

#print add(*map(int, sys.argv[1:]))

#add(*[1,2])
#add(1,2)