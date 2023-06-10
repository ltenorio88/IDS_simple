from scapy.all import sniff

import os
import win32com.client

def get_friendly_names():
    wmi = win32com.client.GetObject ("winmgmts:")
    for adapter in wmi.InstancesOf ("Win32_NetworkAdapter"):
        print (adapter.NetConnectionID, adapter.GUID)

def list_interfaces():
    if os.name == 'nt':  # Windows
        return get_friendly_names()
    else:  # Unix/Linux/Mac
        return get_if_list()  # You will need to define get_if_list for Unix-based systems.



import platform
from scapy.all import get_if_list

def get_os():
    return platform.system()

def list_interfaces():
    return get_if_list()


def capture_packets(interface, packet_count=100):
    """
    Capture packets from the specified network interface.

    Args:
        interface (str): The name of the network interface to capture packets from.
        packet_count (int): The number of packets to capture.

    Returns:
        list: A list of captured packets.
    """
    packets = sniff(iface=interface, count=packet_count)

    return packets
