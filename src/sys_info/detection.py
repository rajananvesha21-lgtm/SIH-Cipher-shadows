import platform
import socket

from .wind.wind import wind
from .mac.mac import mac
from .Linux.Lin import Lin


def detect_system():
    operating_system = platform.system()

    system_info = {
        "OS Version": platform.release(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
    }

    if operating_system == "Windows":
        wind()

    elif operating_system == "Linux":
        Lin()

    elif operating_system == "Darwin":
        mac()

    return system_info