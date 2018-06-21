def f(n):
    li = [1,2,3]
    print 10/n
    print li[n]

try:
    f(2)
    print "Hello"
except IndexError as err:
    print "Wrong index: ", err
except ZeroDivisionError as err:
    print "Cannot divide by 0: ", err
except Exception as err:
    print "Something went wrong: ", err
# try:
#     f(5)
#     print "hello"
# except:
#     print "Something went wrong"


