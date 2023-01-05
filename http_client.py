import socket

HOST = "127.0.0.11"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"GET /comments HTTP/1.1 HOST: hexlet.local\n\n")
    data = s.recv(1024)

print(f"Received {data!r}")

# print(len(str.encode('utf-8')))

