import socket
from threading import Thread
import tkinter as tk
from tkinter import *

host = "10.0.0.143"
port = "312"

def receive():
    while True:
        try:
            msg = s.recv(1024).decode()
            msg_list.insert(tk.end)
        except Exception:
            print("There is an Error Receiving Message")

def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf8"))

