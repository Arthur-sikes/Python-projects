import socket 
import select
HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 8000
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((IP,PORT))
server_socket.listen()
socket_list = [server_socket]
clients = {}
print(f"Listening for connections on {IP}:{PORT}......")
print(socket_list)
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGHT)
        if not len(message_header):
            return False
        message_lenght = int(message_header.decode('utf-8').strip())
        return {'header':message_header,'data':client_socket.recv(message_lenght)}
    except:
        return False
def main():
    while True:
        read_sockets,_,exeption_sockets = select.select(socket_list,[],socket_list)
        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                client_socket,client_adress = server_socket.accept()
                user = recieve_message(client_socket)
                if user is False:
                    sockets_list.append(client_socket)
                    clients[client_socket] = user
                    print("Accepted new connection from {}:{} ,username:{} ".format(*client_adress,user['data'].decode('utf-8')))
                else:
                    message = recieve_message(notified_socket)
                    if message is False:
                        print("Closed connection from {}".format(clients[notified_socket][data.decode('utf-8')]))
                        socket_list.remove(notified_socket)
                        del clients[notified_socket]
                        continue
                        
main()         