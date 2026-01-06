from scapy.all import sniff, IP, TCP, UDP

print("Basic Network Sniffer Started")
print("Capturing live packets...\n")

header = "{:<15} {:<15} {:<6} {:<10} {:<10} {:<6}"
print(header.format(
    "Source IP", "Destination IP", "Proto", "Src Port", "Dst Port", "Size"
))
print("-" * 70)

def capture(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)

        proto = "IP"
        src_port = "-"
        dst_port = "-"

        if packet.haslayer(TCP):
            proto = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            proto = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        print(header.format(
            src_ip, dst_ip, proto, src_port, dst_port, size
        ))

sniff(prn=capture, store=False)
