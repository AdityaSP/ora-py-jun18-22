import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address =('www.google.com', 80)
client.connect(address)
client.send('GET /index.html HTTP/1.0\n\n')

data = []
while True:
    part= client.recv(1000)
    if part:
        data.append(part)
    else:
        break

print "".join(data)

