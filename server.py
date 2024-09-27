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

def broadcast(msg):
    for client in clients:
        client.send(bytes(prefix, "utf8") + msg)

def accept_client_connection():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, " has Connected")
        client_conn.send(bytes("Welcome to the chat room, Please type ypur name to continue", "utf8"))
        Thread(target=handle_clients, args=(client_conn)).start()
        
if __name__ == "__main__":
    sock.listen(3)
    print("listening on port : ", port, ".....")
    t = Thread(target=accept_client_connection)
    t.start()
    t.join()
