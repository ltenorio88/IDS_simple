import threading
from packet_capture import capture_packets
from packet_analysis import analyze_packets
from anomaly_detection import detect_anomalies
from alerts import send_alert
from event_logging.log import log_event

class IDSInterface:
    def __init__(self):
        self.ids_running = False

    def start_ids(self, interface):
        self.ids_running = True
        while self.ids_running:
            packets = capture_packets(interface)
            analyzed_packets = analyze_packets(packets)
            anomalies = detect_anomalies(analyzed_packets)

            if anomalies:
                send_alert(anomalies)
                log_event(anomalies)

    def stop_ids(self):
        self.ids_running = False
        log_event("IDS stopped.")

def start_interface(interface):
    ids_interface = IDSInterface()
    ids_thread = threading.Thread(target=ids_interface.start_ids, args=(interface,))
    ids_thread.start()
    return ids_interface

def stop_interface(ids_interface):
    ids_interface.stop_ids()
