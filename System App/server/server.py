import threading
import socket
import pickle
from util.CONTANTS import *
from service.servicos import Services

HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)  # binds server to host n address


#  handles individual connections in new threads
def handle_client(conn, addr):
    print("[NEW CONNECTION] Client", addr[0], "connected")

    service = Services()

    connected = True
    while connected:
        #  this is just the HEADER
        msg_length = conn.recv(HEADER).decode(FORMAT)  # blocking line

        if msg_length:   # this is checking if client actually sent a msg
            print("-D size: " + msg_length)
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            # this is the actual msg
            if msg == DISCONNECT_MSG:
                connected = False  # it is necessary to stop connection otherwise it may remain on the list of active connections
                print("[TERMINATED] ", addr[0], " ended connection.")

            if msg == REQUEST_CPU:
                service.cpu_service(conn, addr, msg)
                continue

            if msg == REQUEST_MEM:
                service.msn_service(conn, addr, msg)
                continue

            if msg == REQUEST_GATEWAY:
                service.gateway_service(conn, addr, msg)
                continue

            if msg == REQUEST_NET:
                service.internet_service(conn, addr, msg)
                continue

            if msg == REQUEST_PID:
                service.process_service(conn, addr, msg)
                continue

            if msg == REQUEST_DIR:
                service.directory_service(conn, addr, msg)
                continue

            if msg == REQUEST_STAT:
                service.stats_info(conn, addr, msg)
                continue

            if msg == REQUEST_SPACE:
                service.space_info(conn, addr, msg)
                continue

            if msg == REQUEST_IP:
                service.active_connections(conn, addr, msg)
                continue

            if msg == REQUEST_FREQ:
                service.freq_info(conn, addr, msg)
                continue

            #  print IP address and its message
            print(addr, ": ", msg)

            # send it back to the cliente
            conn.recv(pickle.dumps(f"{HOST} : {msg[0:6]}..received"))

    # if connected is False then close conn
    conn.close()


# accepts n starts new connections
def start():
    server.listen(5)

    while True:
        conn, addr = server.accept()  # blocking line, hence new thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()  # starts a new thread
        print("[ACTIVE] Active connections: ", threading.activeCount() -1)


# starts server
print("[STARTED] Server's up on", HOST)
start()
