import socket

host = 'www.google.com'
port = 80

# client = socket.create_connection((host, port))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

data = b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
client.send(data)

data = b''
while True:
    received_data = client.recv(8192)
    if not received_data:
        break
    data += received_data

with open('data.html', 'wb') as file:
    file.write(data)
