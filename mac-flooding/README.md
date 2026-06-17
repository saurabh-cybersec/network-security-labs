# MAC Flooding Lab

CAM table overflow attack on a physical switch using Python raw
sockets — demonstrated on D-Link DES-1005C unmanaged switch.

---

## What I Built

A Python script that:
- Generates random source MAC addresses per packet
- Crafts raw Ethernet frames using `struct.pack`
- Floods the switch via `AF_PACKET, SOCK_RAW` at maximum speed
- Runs continuously until `Ctrl+C`

---

## Lab Setup

| Machine | Role | IP | Interface |
|---------|------|----|-----------|
| Kali Linux | Attacker | 10.10.10.1 | eth1 |
| Ubuntu VM | Victim | 10.10.10.2 | enx... |
| Raspberry Pi 3B+ | Observer | 10.10.10.3 | eth0 |
| D-Link DES-1005C | Physical Switch | — | — |

All machines connected via physical switch through USB-to-Ethernet
adapters.

---

## Attack Flow

Kali sends random MAC frames at maximum rate via eth1
Switch CAM table fills up with fake MAC entries
Switch enters fail-open mode — broadcasts all frames
Pi receives Ubuntu↔Kali traffic it should never see


---

## Wireshark / tcpdump Observations

**On Kali (tcpdump eth1 icmp):**
- Ubuntu→Pi ICMP traffic visible on Kali
- Normally switch sends this directly to Pi — Kali should not see it
- After CAM overflow, switch broadcasts — Kali receives it too

**On Raspberry Pi (tcpdump icmp):**
- Both directions visible: Ubuntu→Pi request AND Pi→Ubuntu reply
- Confirms switch is broadcasting all frames to all ports

**CPU impact:**
- mac_flood.py consumed ~73% CPU on Kali
- /tmp filesystem filled to 100% during extended flood
- Wireshark capture files caused tmpfs exhaustion

---

## Key Learnings

**CAM table behavior** — Switch maintains MAC→Port mapping.
When table is full, new MACs cannot be learned — switch falls
back to broadcasting frames to all ports like a hub.

**Random MAC per packet** — Critical for attack to work.
If same MAC is reused, only one CAM entry is consumed.
`src_mac` and `frame` must be inside the while loop.

**Physical vs Virtual switch** — VMware virtual switch has
no CAM overflow behavior. Physical switch required to
demonstrate this attack.

**tmpfs exhaustion** — `/tmp` is RAM-based (tmpfs). Extended
flooding + Wireshark capture can fill it completely.
Fix: `sudo reboot` clears tmpfs on restart.

**IEEE 802.3 — MAC structure:**
- LSB of first byte = 0 → Unicast
- LSB of first byte = 1 → Multicast/Group
- Random MACs may violate this — cosmetic warning in Wireshark

---

## Tools Used
- Python 3, `socket`, `struct`, `random`
- tcpdump (traffic verification)
- D-Link DES-1005C physical switch
- Kali Linux, Ubuntu VM, Raspberry Pi 3B+

---

## Screenshots
![MAC Flood Running](screenshots/mac_flood_terminal.png)
![Kali tcpdump — Ubuntu-Pi traffic](screenshots/kali_tcpdump_overflow.png)
![Ubuntu ping output](screenshots/ubuntu_ping.png)
![Pi tcpdump — both directions](screenshots/pi_tcpdump.png)

---
