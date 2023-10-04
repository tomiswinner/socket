import socket
import time
import threading

server_ip = 'localhost'
port = 52001
buffer_size = 1024
num_requests = 1000  # Number of requests to send
num_threads = 10     # Number of threads to spawn

lock = threading.Lock()
completed_requests = 0

def send_request():
    global completed_requests
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, port))
        client_socket.send(b'REQUEST')
        client_socket.recv(buffer_size)
    with lock:
        completed_requests += 1

def thread_task():
    for _ in range(num_requests // num_threads):
        send_request()

if __name__ == "__main__":
    start_time = time.time()
    
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=thread_task)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    rps = completed_requests / elapsed_time
    print(f'Handled {rps:.2f} requests per second')

