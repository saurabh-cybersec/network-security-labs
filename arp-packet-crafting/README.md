# ARP Packet Crafting using Python Raw Sockets

## Overview

This project demonstrates manual ARP packet crafting using Python raw sockets on Linux.

The goal of this lab was to understand how ARP works at the packet level by manually building:

- Ethernet headers
- ARP headers
- ARP Request packets (`opcode = 1`)
- ARP Reply packets (`opcode = 2`)

The packets were created using Python's `struct.pack()` and transmitted through raw sockets without using high-level networking libraries like Scapy.

---

## Features

- Manual Ethernet frame construction
- Manual ARP header construction
- ARP Request packet crafting
- ARP Reply packet crafting
- Raw socket packet transmission
- Wireshark packet verification

---

## Project Structure

```text
arp-packet-crafting/
│
├── README.md
│
├── screenshots/
│   ├── arp_request_wireshark.png
│   └── arp_reply_wireshark.png
│
└── src/
    ├── arp_request.py
    └── arp_reply.py