import socket
import threading

from app.p2p.protocol import (
    receive_message,
    send_message
)


class TCPServer:

    def __init__(self, port):
        self.port = port


    def start(self):

        server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        server.bind(
            ("0.0.0.0", self.port)
        )

        server.listen(5)


        print(
            f"[TCP] Server listening on {self.port}"
        )


        while True:

            client, addr = server.accept()

            print(
                f"[TCP] Connection from {addr}"
            )


            thread = threading.Thread(
                target=self.handle_client,
                args=(client,)
            )

            thread.start()



    def handle_client(self, client):

        message = receive_message(client)

        print(
            "[TCP] Received:",
            message
        )


        response = {
            "type": "WELCOME",
            "message": "Connection accepted"
        }


        send_message(
            client,
            response
        )


        client.close()