import socket
#custom IP
host = "10.0.0.143"
port = 312

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
