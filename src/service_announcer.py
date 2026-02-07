import socket
import json
import time
from threading import Thread

class ServiceAnnouncer:
    """Handles broadcasting user presence on the local network via UDP."""
    
    def __init__(self):
        self.username = input("Enter your username: ").strip() [cite: 56]
        # Use subnet broadcast address (e.g., 192.168.1.255) for real networks
        self.broadcast_ip = "192.168.164.255" 
        self.port = 6000

    def start_broadcasting(self):
        """Continuously sends a JSON payload with user info every 8 seconds."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        while True:
            try:
                ip = socket.gethostbyname(socket.gethostname())
                message = json.dumps({"username": self.username, "ip": ip})
                sock.sendto(message.encode('utf-8'), (self.broadcast_ip, self.port))
                time.sleep(8) # Maintain "Online" status in peer discovery
            except Exception as e:
                print(f"Broadcast error: {e}")
                break

if __name__ == "__main__":
    announcer = ServiceAnnouncer()
    Thread(target=announcer.start_broadcasting, daemon=True).start()
    input("Press Enter to stop broadcasting...\n") [cite: 56]
