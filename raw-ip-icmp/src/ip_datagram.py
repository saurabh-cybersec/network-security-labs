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


    src_ip = socket.inet_aton("192.168.100.3")
    dst_ip = socket.inet_aton("192.168.100.4")
    payload = "hello ! , This is a custtom raw ip datagram".encode('utf-8')

    ip_ver = 4
    ip_ihl = 5
    ip_tos = 0
    ip_tot_len = 20 + len(payload)
    ip_id = 12345
    ip_frag_off = 0
    ip_ttl = 128
    ip_proto = 253 #experimental protocol number for testing
    ip_check = 0
    ip_header = struct.pack('!BBHHHBBH4s4s', (ip_ver << 4) + ip_ihl, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, src_ip, dst_ip)

    ip_check = calculate_checksum(ip_header)
    ip_header = struct.pack('!BBHHHBBH4s4s',
    (ip_ver << 4) + ip_ihl, ip_tos, ip_tot_len,
    ip_id, ip_frag_off, ip_ttl, ip_proto,
    ip_check, src_ip, dst_ip)

    datagram = ip_header + payload

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) as raw_socket:
            raw_socket.sendto(datagram, (socket.inet_ntoa(dst_ip), 0))
            print("Raw IP datagram sent successfully.")

    except Exception as error:
        print(f"An error occurred: {error}")            
    except PermissionError:
        print("Permission denied: You need to run this script with administrative privileges.") 
if __name__ == "__main__":
    main()
