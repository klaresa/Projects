import pickle
import socket
from util.CONTANTS import *

HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)  # connects client to the server n port


def send(msg):
    request(msg)  # sends request to the server

    # print(response())  # prints msg from the server when debugging
    return response()  # returns response


# sends a message to the server
def request(msg):
    message = msg.encode(FORMAT)  # encode message to bytes
    msg_length = len(message)
    print("-D size: " + str(msg_length))
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))  # byte format
    client.send(send_length)
    client.send(message)


# receives a response from the server
def response():
    recv = client.recv(20000)
    return pickle.loads(recv)


#use this when debugging
print("We are now connected.")
# print("type !out to disconnect")
# msg = input("..yes?\n")
# while msg != '!out':
#     if msg:
#         send(msg)
#     msg = input()
# print("You are now disconnecting from the server.")

def request_cpu():
    return send(REQUEST_CPU)

def request_mem():
    return send(REQUEST_MEM)

def request_gateway():
    return send(REQUEST_GATEWAY)

def request_net():
    return send(REQUEST_NET)

def request_pid():
    return send(REQUEST_PID)

def request_dir():
    return send(REQUEST_DIR)

def request_stat():
    return send(REQUEST_STAT)

def request_space():
    return send(REQUEST_SPACE)

def request_ip():
    return send(REQUEST_IP)

def request_freq():
    return send(REQUEST_FREQ)
