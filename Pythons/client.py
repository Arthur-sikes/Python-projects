import socket
import errno
from threading import Thread
HEADER_LENGHT = 10
client_socket = None
def connect(ip,port,my_username,error_callback):
    global client_socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client_socket.connect((ip,port))
    except Exception as e:
        error_callback('cobnection error {}'.str(e))
    return False
    user_name = my_username.encode('utf-8')
    username_header = f"{len(username):}"
