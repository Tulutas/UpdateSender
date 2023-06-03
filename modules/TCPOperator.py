import socket
from queue import Queue


class TCPClass():
    """This class will be used a creating TCP Server and Client Applications"""
    def __init__(self,hostname,listen_port):
        self.hostname=hostname
        self.listen_port=listen_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.output_que=Queue()

    def open_tcp_server(self):
        # Bind the socket to the port
        self.server_address = (self.hostname, self.listen_port)
        self.output_que=Queue()
        print ('starting up on port %s',self.server_address)
        self.sock.bind(self.server_address)
    
    def data_received(self,data):
        self.output_que.append(data)
        

    def start_echo_listening(self):
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
    def send_data_to_server(self,remote_ip,remote_port,data):
        self.sock.connect(remote_ip,remote_port)
        self.sock.sendall(b"Hello, world")
        data = self.sock.recv(1024)
        print(str(data))

newobject=TCPClass("127.0.0.1",30001)
newobject.open_tcp_server()
newobject.start_echo_listening()