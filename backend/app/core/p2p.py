import os

from app.p2p.discovery import PeerDiscovery
from app.p2p.tcp_server import TCPServer


TCP_PORT = int(os.getenv("TCP_PORT", "9000"))
DISCOVERY_PORT = int(os.getenv("DISCOVERY_PORT", "9999"))


discovery = PeerDiscovery(
    tcp_port=TCP_PORT,
    discovery_port=DISCOVERY_PORT
)


tcp_server = TCPServer(
    TCP_PORT
)