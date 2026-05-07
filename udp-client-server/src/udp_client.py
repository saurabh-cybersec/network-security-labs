import socket

def main():
    target_host = "server_ip" # Change this to the actual IP address of the UDP server
    target_port = 5060
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = "Hello, UDP server!"
        client_socket.sendto(message.encode(), (target_host, target_port))

        print(f"Sent message to {target_host}:{target_port}: {message}")

        try:
            response_data, server_addr = client_socket.recvfrom(4096)
            response_message = response_data.decode("utf-8", errors="replace")
            print(f"Received response from {server_addr}: {response_message}")
        except socket.timeout:
            print("No response received within timeout period.")
        except Exception as error:
            print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()