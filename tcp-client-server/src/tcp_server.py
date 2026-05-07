import socket

def main():

    host = "0.0.0.0"
    port = 8090

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

            server_socket.bind((host, port))
            server_socket.listen(5)

            print(f"TCP Server is listening on {host}:{port}...")

            while True:

                client_socket, client_address = server_socket.accept()

                print(f"Connection from {client_address} has been established.")

                with client_socket:

                    while True:

                        data = client_socket.recv(1024)

                        if not data:
                            print("No data received. Closing connection.")
                            break

                        decoded_data = data.decode().strip()

                        print(f"Received data: {decoded_data}")

                        response = "Hello from the TCP Server!"

                        client_socket.sendall(response.encode())

                        if decoded_data.lower() in ["exit", "quit"]:
                            print(f"Client {client_address} requested to close the connection.")
                            break

    except KeyboardInterrupt:
        print("\nServer is shutting down gracefully.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()