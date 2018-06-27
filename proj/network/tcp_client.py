import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 9999)
client.connect(address)
data = client.recv(100)
print "Got this from the server", data
client.send('Thank you')