import re, csv
from collections import Counter

with open('/var/log/auth.log') as f:
    ips = re.findall(r'Failed password.*?from (\d+\.\d+\.\d+\.\d+)', f.read())

counts = Counter(ips)

with open('ssh_failures.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['IP Address', 'Failed Attempts'])
    writer.writerows(counts.items())

print("Failed SSH Attempts:", dict(counts))
