import socket
import json


with open('domains.txt') as f:
    domains_list = f.read().split()

    domains_json = []
    for domain in domains_list:
        domains_json.append({
            "name": domain,
            "ip": socket.gethostbyname(domain)
        })

with open('domains.json', 'w') as f:
    f.write(json.dumps(domains_json, indent=4))
