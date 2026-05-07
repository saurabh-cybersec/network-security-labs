import socket

def main():
    host = '10.10.10.2'  # Replace with the actual IP address of the TCP server
    port = 8090
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Connected to TCP Server at {host}:{port}")

            while True:
                message = input("Enter a message (or 'quit' to exit): ")
                if message.strip().lower() in ["quit", "exit"]:
                    client_socket.sendall(message.encode())
                    print("You have requested to close the connection.")
                    break
                client_socket.sendall(message.encode())
                response = client_socket.recv(1024)
                print(f"Server response: {response.decode()}")
    except KeyboardInterrupt:
        print("Client is shutting down gracefully.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()