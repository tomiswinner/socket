import socket
import time

def measure_throughput():
    server_ip = 'localhost'
    port = 52001
    buffer_size = 1024
    total_data_size = 1024 * 1024 * 10  # 100 MB for example
    chunks = total_data_size // buffer_size

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, port))

        data_to_send = b'x' * buffer_size
        start_time = time.time()

        for _ in range(chunks):
            client_socket.send(data_to_send)

        end_time = time.time()

        # Calculate throughput
        elapsed_time = end_time - start_time
        throughput = total_data_size / elapsed_time / (1024 * 1024)  # In MB/s
        print(f'Throughput: {throughput:.2f} MB/s')

if __name__ == "__main__":
    measure_throughput()
