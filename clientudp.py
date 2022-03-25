import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('client socket created success')

host = 'localhost'
port = 5433

message = 'hi server'

try:
    print('client: ' + message)
    s.sendto(message.encode(), (host, 5432))

    data, server1 = s.recvfrom(4096)
    data = data.decode()
    print('client: ' + data)
finally:
    print('client closed connection')
    s.close()
