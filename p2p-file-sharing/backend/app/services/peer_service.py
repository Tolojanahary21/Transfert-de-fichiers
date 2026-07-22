import socket
import platform
import uuid


def get_device_info():

    device_name = socket.gethostname()

    ip_address = socket.gethostbyname(
        socket.gethostname()
    )

    os_name = platform.system()

    device_uuid = str(uuid.uuid4())


    return {
        "device_uuid": device_uuid,
        "device_name": device_name,
        "ip_address": ip_address,
        "port": 8000,
        "os": os_name,
        "status": "ONLINE"
    }