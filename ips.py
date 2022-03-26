import ipaddress


ip = '192.168.0.1'
network = '192.168.0.0/24'
network_fail = '192.168.0.100/24'

address = ipaddress.ip_address(ip)
net = ipaddress.ip_network(network_fail, strict=False)

print(address)
print(network)
print(network_fail)

for ip in net:
    print(ip)
