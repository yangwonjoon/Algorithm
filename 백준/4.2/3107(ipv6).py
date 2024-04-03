import ipaddress

ip = input()
print(ipaddress.IPv6Address(ip).exploded)
