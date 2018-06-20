print "Hello World"

#ip = input('Enter a number:')
#print type(ip)
#print ip
#
#s = raw_input('Enter a string: ')
#print type(s)
#print s

while True:
    i = raw_input("Press y to continue and n to stop").lower()
    if i == 'y' or i == 'n':
        print "User has entered what I wanted"
        break