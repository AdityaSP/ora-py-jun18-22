import ippack.iphelper as iputils

def calculate(ip):
    ip_list= ip.split('.')
    ip_list[-1] = str(int(ip_list[-1])  +1)
    return ".".join(ip_list)
    
ip = raw_input('Enter an ip: ')

if not iputils.validate(ip):
    exit()

print calculate(ip)




#if len(ip.split('.')) != 4:
#    print "Badly formed ip"
#    exit()
#    