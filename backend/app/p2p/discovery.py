import json
import socket
import threading
import uuid

DISCOVERY_PORT = 9999
DEFAULT_DISCOVERY_PORT = 9999
BUFFER_SIZE = 4096


class PeerDiscovery:
    def __init__(
        self,
        tcp_port: int,
        discovery_port: int = 9999
    ):
        self.uuid = str(uuid.uuid4())
        self.hostname = socket.gethostname()
        self.tcp_port = tcp_port
        self.discovery_port = discovery_port

    def get_local_ip(self) -> str:
        """
        Retourne l'adresse IP locale de la machine.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()

        return ip

    def start_listener(self):
        """
        Écoute les requêtes DISCOVER et répond avec les informations du pair.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        except Exception:
            pass

        sock.bind(("", self.discovery_port))

        print(f"[DISCOVERY] Listening on UDP {self.discovery_port}")

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
        """
        Lance le serveur UDP dans un thread.
        """
        thread = threading.Thread(
            target=self.start_listener,
            daemon=True,
        )

        thread.start()

    def discover(self, timeout: int = 3):
        """
        Envoie un broadcast et attend les réponses.
        """
        peers = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        sock.settimeout(timeout)

        message = {
            "type": "DISCOVER"
        }

        sock.sendto(
    json.dumps(message).encode(),
    ("255.255.255.255", self.discovery_port)
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