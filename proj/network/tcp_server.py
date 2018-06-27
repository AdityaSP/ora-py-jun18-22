import socket
import time
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 9999)
server.bind(address)
print "I am now bound to ", address
server.listen(5)
print "I am up and running"

def process_client(client_conn):
    client = client_conn[0]
    client_add = client_conn[1]
    print "Got a connection from ", client_add
    time.sleep(20)
    print "Sending a welcome message"
    client.send("Welcome")
    data = client.recv(100)
    print "client said:", data

while True:
    print "Now I am waiting for a connection"
    client_conn = server.accept()
    t = threading.Thread(target=process_client, args=(client_conn,))
    t.start()