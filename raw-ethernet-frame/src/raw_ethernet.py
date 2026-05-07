import socket

def main():
    interface = "eth0"  

    def frame():
        dst_mac = bytes.fromhex('ff ff ff ff ff ff') #this is the broadcast MAC address
        src_mac = bytes.fromhex('00 11 22 33 44 55') #change to your own MAC address
        ethertype = bytes.fromhex('09 00')
        payload = b'Hello, this is a Experimental raw Ethernet frame!'  
        return dst_mac + src_mac + ethertype + payload
    
    try:
        with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as raw_socket:
            raw_socket.bind((interface, 0))
            raw_socket.send(frame())
            print("Raw Ethernet frame sent successfully.")
    
    except PermissionError:
        print("Permission denied: You need to run this script with elevated privileges (e.g., as root).")
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
    