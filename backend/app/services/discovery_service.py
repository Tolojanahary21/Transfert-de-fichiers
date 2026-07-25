import threading

from app.sockets.udp.listener import (
    start_listener
)

from app.sockets.udp.broadcaster import (
    discover_peers
)


def start_discovery():

    threading.Thread(

        target=start_listener,

        daemon=True

    ).start()


    discover_peers()