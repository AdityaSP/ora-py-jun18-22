# fh = open('trial.txt', 'wt')
# fh.write('new line')
# fh.close()

# fh = open('trial1.txt', 'at')
# fh.write('some other things\n')
# fh.write('some other things\n')
# fh.write('some other things\n')
# fh.close()

#p = 'C:\\Users\\Dell lap\\Desktop\\Python\\oracle\\online\\jun18-22\\proj\\trial.txt'
#p = 'C:/Users/Dell lap/Desktop/Python/oracle/online/jun18-22/proj/trial.txt'
p = r'C:\Users\Dell lap\Desktop\Python\oracle\online\jun18-22\proj\trial.txt'
fh = open(p, 'rt')
print "First read"
s = fh.read()
print s
fh.seek(0)
print 'Second read'
s = fh.read()
print s

# l = fh.readlines()
# print l
#
# for line in fh:
#     print line

fh.close()




