This project is a simple UDP client-server communication lab built using Python sockets.

The UDP server was tested on an Ubuntu virtual machine and the client was tested on a Kali Linux virtual machine inside a custom networking lab environment.

I used this project to understand:

UDP socket communication
sendto() and recvfrom()
connectionless communication
UDP packet flow in Wireshark
timeout handling using Python sockets
packet transmission between Linux virtual machines
Lab Setup
Machine	Purpose
Ubuntu VM	UDP Server
Kali Linux VM	UDP Client
Wireshark	Packet Analysis

Both virtual machines were connected using VMware NAT networking.

Features
UDP datagram communication
Server response handling
Timeout handling
UTF-8 payload decoding
Wireshark packet capture analysis
Project Structure
udp-client-server/
│
├── README.md
│
├── screenshots/
│   ├── udp_client_communication.png
│   ├── udp_server_session.png
│   └── wireshark_capture_udp_communication.png
│
└── src/
    ├── udp_client.py
    └── udp_server.py
Running the Lab
Start the UDP Server
python3 udp_server.py
Run the UDP Client

Update the target IP address inside udp_client.py if required.

python3 udp_client.py
Wireshark Analysis

Display filter used:

udp.port == 5060

Observed:

UDP communication without a handshake
Source and destination ports
UDP payload exchange between the client and server
Packet length and payload data
Screenshots
UDP Client Communication

Shows successful message transmission and server response.

UDP Server Session

Shows packet reception and payload details.

Wireshark UDP Packet Capture

Shows UDP request and response packets exchanged between the two virtual machines.