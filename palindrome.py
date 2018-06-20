i = raw_input("Enter a string: ").upper()

print "-" * 30
if i == i[::-1]:
    print "Its a palindrome!"
else:
    print "Not a palindrome!"
print "-" * 30
