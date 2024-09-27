import socket
# import required libraries
import socket
from threading import Thread
import tkinter
from tkinter import *

def receive():
    while True:
        try:
            msg = s.recv(1024).decode()
            msg_list.insert(tkinter.END, msg)
        except Exception:
            print("There is an Error Receiving Message")

def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf8"))


window = Tk()
window.title("Chat Application")
window.configure(bg="green")

message_frame = Frame(window, height=100, width=100, bg='white')
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg="white", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

entry_field = Entry(window, textvariable=my_msg, fg="black", width=50)
entry_field.pack()

send_button = Button(window, text="Send", font="Aerial", fg="black", bg="blue", command=send)
send_button.pack()

host = "10.0.0.143"
port = 312

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

receive_thread = Thread(target=receive)
receive_thread.start()

mainloop()