# Raw Ethernet Frame Crafting Lab

This project demonstrates manual Ethernet frame crafting using Python raw sockets on Linux.

The frame was broadcast from a Kali Linux VM and captured on an Ubuntu VM using Wireshark inside a VMware lab environment.

I used this project to understand:
- Ethernet frame structure
- Layer 2 communication
- AF_PACKET raw sockets
- broadcast frame transmission
- custom EtherType testing
- packet analysis in Wireshark

---

## Notes

- This project is Linux only because it uses `AF_PACKET` raw sockets.
- Root privileges are required to create and send raw Ethernet frames.
- The Ethernet header was crafted manually inside the script.
- A custom experimental EtherType (`0x0900`) was used for local testing.

---

## Lab Setup

| Machine | Purpose |
|---|---|
| Kali Linux VM | Raw Ethernet frame sender |
| Ubuntu VM | Wireshark packet capture |
| VMware NAT Network | Internal lab communication |

---

## Features

- Manual Ethernet frame construction
- Custom source and destination MAC addresses
- Broadcast frame transmission
- Experimental EtherType usage
- Raw socket communication using Python
- Wireshark frame inspection

---

## Project Structure

```text
raw-ethernet-frame/

├── README.md
├── screenshots/
│   ├── frame_sent_successfully.png
│   └── wireshark_capture_raw.png
│
|
│
└── src/
    └── raw_ethernet.py