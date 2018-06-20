import subprocess

def getmem(line):
    mem = line.split()[-2]
    return int(mem.replace(',',''))

output = subprocess.check_output('tasklist', shell=True).split("\r\n")


#for line in sorted(output[3:-1], key = getmem, reverse=True)[:3]:
#    print line

# fh = open('top.log', 'wt')
# fh.write("\n".join(sorted(output[3:-1], key = getmem, reverse=True)[:3]))
# fh.close()


with open('top.log', 'wt') as fh:
    fh.write("\n".join(sorted(output[3:-1], key=getmem, reverse=True)[:3]))

print "Created"

