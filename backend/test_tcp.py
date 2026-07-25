from app.p2p.tcp_server import TCPServer
from app.p2p.tcp_client import connect_peer

import threading
import time



server = TCPServer(9000)


threading.Thread(
    target=server.start,
    daemon=True
).start()


time.sleep(1)


connect_peer(
    "127.0.0.1",
    9000
)