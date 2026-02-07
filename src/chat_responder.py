import socket
import json
import threading
from pyDes import triple_des, PAD_PKCS5

class ChatResponder:
    """Listens for incoming TCP connections on port 6001.""" [cite: 64]
    
    def __init__(self):
        self.port = 6001
        self.username = "Responder"

    def handle_client(self, conn, addr):
        """Handles session logic and decryption for an individual client."""
        print(f"Connection established with {addr}")
        # Secure/Unsecure message handling logic...

    def start_listening(self):
        """TCP server loop.""" [cite: 64]
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', self.port))
            s.listen()
            print(f"Listening for chats on port {self.port}...")
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    responder = ChatResponder()
    choice = input("Responder Options: Listen | Exit: ").strip().lower() [cite: 64]
    if choice == "listen":
        responder.start_listening()
