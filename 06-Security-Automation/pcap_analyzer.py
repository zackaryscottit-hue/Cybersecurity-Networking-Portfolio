from scapy.all import *
from collections import Counter

pkts = rdpcap("capture.pcap")

protocols = Counter()
ips = Counter()

for p in pkts:
    if IP in p:
        ips[p[IP].src] += 1
        for proto in (TCP, UDP, ICMP):
            if proto in p:
                protocols[proto.__name__] += 1

result = f"Protocols: {dict(protocols)}\nTop IPs: {ips.most_common(5)}"

print (result)
open("traffic_summary.txt", "w").write(result)
