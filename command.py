import subprocess

# fire and forget
# subprocess.call('dir', shell=True)

#checks for the exit status. if non -zero raises an error
#subprocess.check_call('move a.txt b.txt', shell=True)


#capture the output of the command
output = subprocess.check_output('dir', shell = True)

print "-------------------------"
print "This is what I collected"
print output
print type(output)
