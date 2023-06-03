import socket
from queue import Queue
import threading
import time

class TCPClass():
    """This class will be used a creating TCP Server and Client Applications"""
    def __init__(self,hostname,listen_port):
        self.hostname=hostname
        self.listen_port=listen_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.output_que=Queue()

    def open_tcp_socket(self):
        # Bind the socket to the port
        self.server_address = (self.hostname, self.listen_port)
        self.output_que=Queue()
        self.input_que=Queue()
        print ('starting up on port %s',self.server_address)
        self.sock.bind(self.server_address)
    
    def data_received(self,data):
        self.output_que.put_nowait(data)
        

    def _start_echo_listening(self):
        """ This function listens a socket and returns echo messsage"""
        self.sock.listen(1)
        while True:
            connection, client_address = self.sock.accept()
            try:
                print('client connected:', client_address)
                while True:
                    data = connection.recv(16)
                    print('received "%s"' , data)
                    if data:
                        self.data_received(data)
                        connection.sendall(data)
                    else:
                        break
            finally:
                connection.close()

    def start_listening(self):
        self.listenthread = threading.Thread(target=self._start_listening,).start()
    def _start_listening(self):
        """ This function listens a socket """
        self.sock.listen(1)
        while True:
            connection, client_address = self.sock.accept()
            try:
                print('client connected:', client_address)
                while True:
                    data = connection.recv(16)
                    print('received "%s"' , data)
                    if data:
                        self.data_received(data)
                    else:
                        break
            finally:
                connection.close()
    def start_connection_to_remote(self,remote_ip,remote_port):
        self.sock.connect(remote_ip,remote_port)
    def connect_to_server(self,remote_ip,remote_port):
        self.sock.connect((remote_ip, remote_port))
    def send_data_to_all(self,data):
        self.sock.sendall(data)

