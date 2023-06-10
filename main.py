from packet_capture import capture_packets, get_os, list_interfaces
from packet_analysis import analyze_packets
from anomaly_detection import detect_anomalies
from alerts import send_alert
from event_logging import log_event
from ui import start_interface, stop_interface

def main():
    os_type = get_os()
    print(f"Detected OS: {os_type}")
    interfaces = list_interfaces()
    print("Available network interfaces:")
    for i, interface in enumerate(interfaces):
        print(f"{i}. {interface}")
    interface_number = int(input("Select the interface number to listen on: "))
    interface = interfaces[interface_number]
    start_interface(interface)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Intrusion Detection System.')
    parser.add_argument('command', type=str, help='Command to run the IDS. Available commands: "start", "stop"')

    args = parser.parse_args()

    if args.command.lower() == 'start':
        main()
    elif args.command.lower() == 'stop':
        stop_interface()
    else:
        print(f'Unknown command: {args.command}')
