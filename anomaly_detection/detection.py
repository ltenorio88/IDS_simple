from scapy.all import IP

def detect_anomalies(packets, target_ip):
    """
    Detect anomalies in a list of packets.

    Args:
        packets (list): The list of packets to analyze.

    Returns:
        list: A list of anomalies.
    """
    anomalies = []

    for packet in packets:
        print("Checking packet: ", packet.summary())
        if IP in packet and packet[IP].src == target_ip:
            print("Anomaly detected in packet: ", packet.summary())
            anomalies.append(packet)

    return anomalies
