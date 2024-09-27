import socket
from threading import Thread
#custom IP
host = "10.0.0.143"
port = 312

clients = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))

def handle_clients(conn):
    name = conn.recv(1024).decode()
    opt1 = f"Fuck off {name}. You suck."
    opt2 = f"Welcome {name}. Good to see you :)"
    
    conn.send(bytes(opt1, "utf8"))
    msg = name + " has joined us"
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name
    while True:
        msg = conn.recv(1024)
        broadcast(msg, name + ":")
        