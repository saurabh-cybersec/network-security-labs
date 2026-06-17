import socket
import struct
import random

def random_mac():
    return ':'.join(f"{random.randint(0, 255):02x}" for _ in range(6))

def main ():
    interface = input("Enter the network interface (e.g., eth0): ").strip().lower()
    dst_mac = bytes.fromhex("ffffffffffff")
    src_mac = bytes.fromhex(random_mac().replace(":", ""))
    ether_type = 0x0900

    payload = b"Hello, this is a test payload for MAC spoofing."

    frame = struct.pack("!6s6sH", dst_mac, src_mac, ether_type) + payload

    try:
        with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as raw_socket:
            raw_socket.bind((interface, 0))
            raw_socket.send(frame)
            print(f"Sent frame with spoofed MAC: {src_mac.hex(':')}")
    except PermissionError:
        print("Permission denied: You need to run this script with elevated privileges (e.g., as root).") 
    except Exception as error:
        print(f"An error occurred: {error}")
if __name__ == "__main__": main()          