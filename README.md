# P2P Secure Chat System (CMP 2204)

This project is a decentralized, peer-to-peer (P2P) messaging system developed using Python. It demonstrates the practical implementation of socket programming, multithreading, and cryptographic protocols without the need for a central server.

## 🚀 Key Features

* **Decentralized Architecture:** Uses UDP broadcasting for automated peer discovery on local networks, eliminating the need for a central server.
* **Secure Communication:** Implements **Diffie-Hellman Key Exchange** and **Triple DES (3DES)** encryption via the `pyDes` library to ensure end-to-end message security.
* **Real-time Chat:** Facilitates reliable, low-latency communication over TCP (port 6001).
* **Message History:** Automatically logs all sent and received messages to local files for session persistence.

## 🛠️ Tech Stack

* **Language:** Python 3.12.10 (Optimized for this version)
* **Development Environment:** Windows 10/11 using VS Code and Spyder
* **Libraries:** `socket`, `threading`, `json`, `pyDes`, `base64`
* **Analysis Tools:** Wireshark (Used for network traffic and packet level verification)

## 🏗️ Project Components

The system is designed with a modular approach consisting of four main modules:
1.  **Service Announcer:** Broadcasts the user's presence and IP address to the local network.
2.  **Peer Discovery:** Listens for broadcasts and maintains an active list of online peers.
3.  **Chat Initiator:** Manages the main user interface, peer selection, encryption mode, and session initiation.
4.  **Chat Responder:** Listens for incoming TCP requests and handles multi-threaded message processing.



## 📡 Network Analysis (Wireshark)

System security and protocol integrity were verified at the packet level to ensure robust communication:
* **TCP Handshake:** Confirmed successful 3-way handshakes on port 6001 for all chat sessions.
* **Payload Encryption:** Verified that JSON payloads are fully encrypted during "Secure Chat" mode, ensuring that no plain-text data is exposed during transit.

## ⚠️ Challenges & Lessons Learned

* **Version Compatibility:** Identified significant output differences between Python 3.13.3 and 3.12.10, leading to the decision to standardize the project on version 3.12.10.
* **Concurrency & UI:** Resolved terminal interface bugs and synchronization issues between the various module listeners.
* **Cryptographic Implementation:** Successfully integrated the `pyDes` library for secure key exchange and messaging after overcoming initial handshake challenges.

## 👥 Team & Contributions

* **Kaan Bircan:** Developed the Chat Initiator and Chat Responder modules.
* **Yakup Nail Ceylan:** Developed the Service Announcer and Peer Discovery modules; conducted Wireshark analysis.
* **Erke Alkım:** Contributed to the Chat Responder module, code optimization, and documentation.

## 📄 License

Distributed under the **MIT License**. See the `LICENSE` file for more information.
