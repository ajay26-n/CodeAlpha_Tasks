from scapy.all import sniff, IP, TCP
from datetime import datetime
from collections import defaultdict


connection_count = defaultdict(set)
THRESHOLD = 10


def detect_intrusion(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        connection_count[src_ip].add(dst_port)

        if len(connection_count[src_ip]) > THRESHOLD:
            print_alert(src_ip)


def print_alert(src_ip):
    print("\n🚨 INTRUSION ALERT 🚨")
    print(f"Time          : {datetime.now()}")
    print(f"Suspicious IP : {src_ip}")
    print(f"Ports Accessed: {len(connection_count[src_ip])}")
    print("Possible Port Scanning Detected!")
    print("-" * 40)


def start_sniffing():
    print("Monitoring traffic... Press Ctrl+C to stop.")
    sniff(prn=detect_intrusion, store=0)


if __name__ == "__main__":
    start_sniffing()

