import socket
import json
import time
import os
from threading import Thread

class PeerDiscovery:
    """Listens for peer broadcasts and updates the active users list."""
    
    def __init__(self):
        self.peers = {} # {ip: {"username": str, "last_seen": float}}
        self.port = 6000
        self.stale_threshold = 20 # Marks as "Away" or removes after 20s [cite: 57]

    def listen(self):
        """UDP listener for discovery packets."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', self.port))

        while True:
            data, addr = sock.recvfrom(1024)
            try:
                msg = json.loads(data.decode('utf-8'))
                username = msg.get("username")
                if username:
                    self.peers[addr[0]] = {"username": username, "last_seen": time.time()}
            except json.JSONDecodeError:
                continue

    def update_ui(self):
        """Periodically refreshes the terminal with active users."""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Peer Discovery - Active Users]") [cite: 57]
            now = time.time()
            with open("peers.txt", "w") as f:
                for ip, info in self.peers.items():
                    elapsed = now - info['last_seen']
                    if elapsed <= self.stale_threshold:
                        status = "Online" if elapsed <= 10 else "Away"
                        print(f"- {info['username']} ({status})")
                        f.write(f"{info['username']},{ip},{info['last_seen']}\n")
            time.sleep(5)

if __name__ == "__main__":
    discovery = PeerDiscovery()
    Thread(target=discovery.listen, daemon=True).start()
    discovery.update_ui()
