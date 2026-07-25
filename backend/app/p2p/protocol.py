import json
import socket
import threading
import uuid


DISCOVERY_PORT = 9999
BUFFER_SIZE = 4096


class PeerDiscovery:

    def __init__(self, tcp_port: int):
        self.uuid = str(uuid.uuid4())
        self.hostname = socket.gethostname()
        self.tcp_port = tcp_port

    def get_local_ip(self):
        """
        Retourne l'adresse IP locale.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip

    def start_listener(self):

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind(("", DISCOVERY_PORT))

        print(f"Discovery server listening on UDP {DISCOVERY_PORT}")

        while True:

            data, addr = sock.recvfrom(BUFFER_SIZE)

            try:
                message = json.loads(data.decode())
            except Exception:
                continue

            if message.get("type") != "DISCOVER":
                continue

            response = {
                "type": "DISCOVER_RESPONSE",
                "uuid": self.uuid,
                "hostname": self.hostname,
                "ip": self.get_local_ip(),
                "port": self.tcp_port,
            }

            sock.sendto(json.dumps(response).encode(), addr)

    def start(self):

        thread = threading.Thread(
            target=self.start_listener,
            daemon=True
        )

        thread.start()
#Le client decouvre
    def discover(self, timeout=3):

        peers = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        sock.settimeout(timeout)

        message = {
            "type": "DISCOVER"
        }

        sock.sendto(
            json.dumps(message).encode(),
            ("<broadcast>", DISCOVERY_PORT)
        )

        while True:

            try:

                data, _ = sock.recvfrom(BUFFER_SIZE)

                peer = json.loads(data.decode())

                if peer["uuid"] != self.uuid:
                    peers.append(peer)

            except socket.timeout:
                break

        sock.close()

        return peers
#connexion entre pairs 
def send_message(sock, message):
    data = json.dumps(message).encode()

    sock.sendall(data)


def receive_message(sock):
    data = sock.recv(4096)

    if not data:
        return None

    return json.loads(data.decode())