"""
Manual ARP request packet crafting using Python raw sockets.
"""
import socket
import struct

def main():

    def get_ethernet_header():
        # Ethernet header fields
        dest_mac = bytes.fromhex("ff ff ff ff ff ff")   #Broadcast MAC address
        src_mac = bytes.fromhex("00 11 22 33 44 55")    #Source MAC address (example)   
        eth_type = 0x0806  # ARP protocol type
        ethernet_header = struct.pack("!6s6sH", dest_mac, src_mac, eth_type)
        return ethernet_header
    
    def get_arp_header():
        # ARP header fields
        htype = 1          
        ptype = 0x0800     
        hlen = 6           
        plen = 4           
        opcode = 1         # ARP request
        sender_mac = bytes.fromhex("00 11 22 33 44 55")    # Sender MAC address 
        sender_ip = socket.inet_aton("192.168.10.3")      # Sender IP address 
        target_mac = bytes.fromhex("00 00 00 00 00 00")    # Target MAC address 
        target_ip = socket.inet_aton("192.168.10.2")        # Target IP address

        arp_header = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, opcode, sender_mac, sender_ip, target_mac, target_ip)
        return arp_header
    
    try:
        # Create a raw socket
        interface = "eth0"  # update based on environment
        with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as raw_socket:
            raw_socket.bind((interface, 0))

            # Construct Ethernet and ARP headers
            frame = get_ethernet_header() + get_arp_header()
            # Send the ARP request
            raw_socket.send(frame)
            print("ARP request sent successfully.")
            
    except PermissionError:
        print("Permission denied: You need to run this script with elevated privileges (e.g., as root).")
    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":    main()
