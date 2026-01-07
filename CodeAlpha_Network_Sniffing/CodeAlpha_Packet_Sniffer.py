from scapy.all import sniff, IP, TCP, UDP
import time

print("Website Traffic Sniffer Started")
print("This will ONLY show packets when you browse websites")
print("It ignores all background traffic\n")
print("Waiting for you to browse a website...")
print("Open Chrome/Firefox and visit any website")
print("-" * 60)


print("Source IP       Destination IP  Proto  Src Port  Dst Port  Size")
print("-" * 70)


packet_counter = 0
packet_limit = 20


website_ports = [80, 443]


def process_packet(packet):
    global packet_counter
    
   
    if packet.haslayer(IP):
       
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        packet_size = len(packet)
        
       
        protocol = "IP"
        source_port = "-"
        destination_port = "-"
        
       
        if packet.haslayer(TCP):
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport
        
     
        elif packet.haslayer(UDP):
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport
        else:
            return  
     
        if destination_port in website_ports or source_port in website_ports:
          
            print(f"{source_ip:15} {destination_ip:15} {protocol:6} {str(source_port):10} {str(destination_port):10} {packet_size:6}")
            
           
            packet_counter += 1
            
           
            if packet_counter >= packet_limit:
                print(f"\n✓ Captured {packet_counter} website packets.")
                print("Stopping now...")
                exit()

time.sleep(3)

try:
  
    sniff(filter="tcp", prn=process_packet, store=False, timeout=60)
    
    if packet_counter == 0:
        print("\nNo website traffic detected.")
        print("Did you visit a website while this was running?")
        print("Make sure you browse to http:// or https:// sites")
    
except KeyboardInterrupt:
    print(f"\n\nStopped by user. Website packets captured: {packet_counter}")
    
except Exception as error:
    print(f"Error: {error}")
    print("Make sure you run as Administrator!")