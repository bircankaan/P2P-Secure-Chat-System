# WARP: Secure P2P Chat System (CMP 2204) 🛡️

This project is a decentralized, peer-to-peer (P2P) messaging system developed using **Python**. It demonstrates the practical implementation of **socket programming**, **multithreading**, and **cryptographic protocols** without the need for a central server. The system is engineered to run on a multi-terminal architecture per client to ensure distinct process management and network stability.

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.12.10-blue)
![Network](https://img.shields.io/badge/Network-TCP%2FUDP-orange)
![Security](https://img.shields.io/badge/Security-pyDes%20Encryption-red)

## 🚀 Key Features

* **Decentralized Architecture:** Uses **UDP broadcasting** for automated peer discovery on local networks, eliminating the need for a central registry or server.
* **Secure Communication:** Implements **Triple DES (3DES)** encryption via the `pyDes` library to ensure end-to-end message security.
* **Real-time Chat:** Facilitates reliable, low-latency communication over **TCP (Port 6001)**.
* **Message History:** Automatically logs all sent and received messages to local files for session persistence and auditing.

## 🛠️ Tech Stack

* **Language:** Python 3.12.10 (Optimized for performance and compatibility)
* **Environment:** Windows 10/11, VS Code, Spyder
* **Core Libraries:** `socket`, `threading`, `json`, `pyDes`, `base64`
* **Analysis Tools:** Wireshark (Used for packet-level verification and traffic analysis)

## 🏗️ System Architecture & Components

The system is engineered as a modular suite of four distinct processes that run concurrently:

| Module | Protocol | Functionality |
| :--- | :---: | :--- |
| **Service Announcer** | **UDP** | Broadcasts the user's presence and IP address to the local network to remain discoverable. |
| **Peer Discovery** | **UDP** | Listens for incoming broadcasts and maintains a dynamic, real-time list of online peers. |
| **Chat Initiator** | **TCP** | The main UI module. Handles user selection, encryption toggles (Secure/Unsecure), and session start. |
| **Chat Responder** | **TCP** | A multi-threaded server listening on **Port 6001** to accept and process incoming message requests. |

## 📡 Network Analysis (Wireshark)

System integrity and security protocols were verified at the packet level:
* **TCP Handshake:** Confirmed successful 3-way handshakes for every chat initiation on Port 6001.
* **Payload Encryption:** Verified that JSON-formatted payloads are fully obfuscated during "Secure Chat" mode, preventing plain-text exposure of sensitive communication.

> **Visual Proof:** Wireshark captures (stored in the assets folder) demonstrate the encrypted data stream and protocol headers during active sessions.
>
> <img src="assets/wireshark_proof.jpg" alt="Wireshark Analysis" width="800"/>

## ⚠️ Engineering Challenges & Solutions

* **Version Compatibility:** Identified critical discrepancies in output behavior between Python 3.13.3 and 3.12.10. The project was standardized on **3.12.10** to ensure cross-platform reliability.
* **Concurrency Management:** Addressed terminal synchronization issues and "stale UI" states by implementing robust, non-blocking multithreaded loops for each network listener.
* **Cryptographic Implementation:** Successfully integrated the `pyDes` library for secure messaging after overcoming initial challenges with block size and padding.

## 🚀 Installation & Usage

To simulate a full P2P node, open **4 separate terminals** and execute the modules in the following specific order:

```bash
# Terminal 1: Broadcast your presence
python src/service_announcer.py

# Terminal 2: Discover active peers in the network
python src/peer_discovery.py

# Terminal 3: Start the server to listen for messages
python src/chat_responder.py

# Terminal 4: Launch the main chat interface
python src/chat_initiator.py
```
## 👥 Team & Contributions

* **Kaan Bircan:** Lead Developer for Chat Initiator and Chat Responder modules.
* **Yakup Nail Ceylan:** Developed Service Announcer, Peer Discovery, and performed Wireshark analysis.
* **Erke Alkım:** Contributed to Chat Responder logic, code optimization, and documentation.

## 📄 License

Distributed under the **MIT License**. See the `LICENSE` file for more information.
