def oct_count(ip):
    ret = True
    if ip.count('.') != 3:
        print "Badly formed ip"
        ret = False
    return ret

def in_range(ip):
    ret = True
    ip_list= ip.split('.')
    for part in ip_list:
        if not (0 < int(part) <= 255):
            print "Wrong value @", part
            ret = False
    return ret

def validate(ip):
    return oct_count(ip) and in_range(ip)