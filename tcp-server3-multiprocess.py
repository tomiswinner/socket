import socket
from multiprocessing import Process

def handle_client(client, address):
    print('Connected client ip : {}'.format(address))
    while True:
        try:
            rcv_data = client.recv(1024)
            if not rcv_data:  # If client closes the connection
                break
            print('Data : {}'.format(rcv_data.decode("utf-8")))
            client.send('Hi!'.encode("utf-8"))
        except ConnectionResetError:  # If client forcefully breaks the connection
            break
    client.close()

if __name__ == "__main__":
    server_ip = 'localhost'
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind((server_ip, 52001))
    tcp_server.listen(5)  # Increased the backlog to 5 for handling more simultaneous clients
    print('Wait tcp accepting...')
    while True:
        client, address = tcp_server.accept()
        process = Process(target=handle_client, args=(client, address))
        process.start()
