import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"
        
        print(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {protocol}")
        with open("packet_log.txt", "a") as log_file:
            log_file.write(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {protocol}\n")

print("Starting packet sniffer...")
scapy.sniff(prn=packet_callback, store=False)
