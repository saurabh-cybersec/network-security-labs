"""
Manual ARP reply packet crafting using Python raw sockets.
"""

import socket
import struct
def main():

    def get_ethernet_header():
        # Ethernet header
        dest_mac = bytes.fromhex('00 11 22 33 44 55')  # Destination MAC address 
        src_mac = bytes.fromhex('00 11 22 33 55 66')   # Source MAC address 
        eth_type = struct.pack('!H', 0x0806)
        
        ethernet_header = dest_mac + src_mac + eth_type
        return ethernet_header
    def get_arp_header():
        # ARP header
        htype = 1
        ptype = 0x0800
        hlen = 6
        plen = 4
        opcode = 2  # ARP reply
        sender_mac = bytes.fromhex('00 11 22 33 55 66')   # Source MAC address 
        sender_ip = socket.inet_aton('192.168.10.2')  # Sender IP address 
        target_mac = bytes.fromhex('00 11 22 33 44 55')  # Target MAC address 
        target_ip = socket.inet_aton('192.168.10.3')  # Target IP address 

        arp_header = struct.pack('!HHBBH6s4s6s4s', htype, ptype, hlen, plen, opcode, sender_mac, sender_ip, target_mac, target_ip)
        return arp_header               
    try:
        # Create a raw socket
        interface = "eth0"  # update based on environment
        with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as raw_socket:
            raw_socket.bind((interface, 0))

            # Construct Ethernet and ARP headers
            frame = get_ethernet_header() + get_arp_header()
            # Send the ARP reply
            raw_socket.send(frame)
            print("ARP reply sent successfully.")

    except PermissionError:
        print("Permission denied: You need to run this script with elevated privileges (e.g., as root).")
    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__": main()
