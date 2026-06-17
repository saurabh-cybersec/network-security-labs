import socket 
import struct

def calculate_checksum(data):
    if len(data) % 2 != 0:
        data += b'\x00'

    total = 0

    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        total += word

    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)

    checksum = ~total & 0xFFFF

    return checksum

def main():

    type = 8  
    code = 0
    checksum = 0
    icmp_header = struct.pack('!BBH', type, code, checksum)

    payload = "hello ! , This is a custtom raw icmp datagram".encode('utf-8')

    checksum = calculate_checksum(icmp_header + payload)
    icmp_header = struct.pack('!BBH', type, code, checksum)                 

    datagram = icmp_header + payload    

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as raw_socket:
            raw_socket.sendto(datagram, ("8.8.8.8", 0))
            print("Raw ICMP datagram sent successfully.")       

    
    except Exception as error:
        print(f"An error occurred: {error}")
    except PermissionError:
        print("Permission denied: You need to run this script with administrative privileges.")             
if __name__ == "__main__":
    main()                    
    
