import socket

from app.p2p.protocol import (
    send_message,
    receive_message
)


def connect_peer(ip, port):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:
        sock.connect(
            (ip, port)
        )

        hello = {
            "type": "HELLO",
            "message": "Hello from peer"
        }

        send_message(
            sock,
            hello
        )

        response = receive_message(sock)

        return {
            "status": "connected",
            "response": response
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        sock.close()