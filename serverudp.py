import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("created client success")

host = 'localhost'
port = 5432

s.bind((host, port))
message = '\nServer: Hi client'

while True:
    data, end = s.recvfrom(4096)
    if data:
        print('server sending message')
        s.sendto(data + (message.encode()), end)
