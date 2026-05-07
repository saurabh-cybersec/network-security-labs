import socket

HOST = "0.0.0.0"
PORT = 5060
BUFFER_SIZE = 4096
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))

        print(f"UDP server listening on {HOST}:{PORT}")

        while True:
            try:
                client_data, client_addr = server_socket.recvfrom(BUFFER_SIZE)

                message = client_data.decode("utf-8", errors="replace")

                print(f"Received message from {client_addr}: {message}")
                print(f"[+] {len(client_data)} bytes received")

                response = "Hello from UDP server!"
                server_socket.sendto(response.encode(), client_addr)

            except socket.timeout:
                print("No packets received within timeout period.")
                continue
            except KeyboardInterrupt:
                print("UDP server shutting down.")
                break
            except Exception as error:
                print(f"An error occurred: {error}")
                break
        

if __name__ == "__main__":    
    main()
    