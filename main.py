import sys
from packet_capture.capture import start_capture
from anomaly_detection.detection import detect_anomalies
from alerts.alert import alert_user
from event_logging.log import log_event
from ui.interface import get_interface

def start_interface(interface, target_ip):
    print("Start capturing packets on interface: ", interface)
    packets = start_capture(interface)
    print("Finished capturing packets. Total packets captured: ", len(packets))
    anomalies = detect_anomalies(packets, target_ip)
    print("Finished detecting anomalies. Total anomalies detected: ", len(anomalies))
    for anomaly in anomalies:
        alert_user(anomaly)
        log_event(anomaly)

def main():
    print("IDS is starting")
    if len(sys.argv) > 1 and sys.argv[1] == 'start':
        interface = get_interface()
        target_ip = input("Enter the IP address to be analyzed: ")
        print("Starting packet capture and analysis on interface: ", interface)
        start_interface(interface, target_ip)
    else:
        print("No valid arguments provided. Please use 'start' to start the IDS.")
    print("IDS is stopping")

if __name__ == "__main__":
    main()
