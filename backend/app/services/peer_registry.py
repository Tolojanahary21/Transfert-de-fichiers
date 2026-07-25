import threading
from datetime import datetime


class PeerRegistry:

    def __init__(self):

        self.peers = {}

        self.lock = threading.Lock()


    def add_peer(self, peer: dict):

        with self.lock:

            peer["last_seen"] = datetime.now()

            self.peers[
                peer["device_uuid"]
            ] = peer


    def get_peers(self):

        with self.lock:

            return list(
                self.peers.values()
            )


peer_registry = PeerRegistry()