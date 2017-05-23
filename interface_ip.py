import re

# supply file with file path to a show run of your NXOS device
file = 'C:\\Scripts\\your-showrun.txt'
# TODO: add paramiko connection to connect to a list of devices
# updated on 5/9/2017 refactored to git rid of multiple regex statements  - gets all ip address's while ignoring subnets

# gather interface ip address
host_object = re.compile('^\s+ip (?:address )?([\d\.]+)$', re.MULTILINE)

file_in = open(file, 'r')
file_in = file_in.read()

# create list of IP's
ip_match = [m.group(1) for m in host_object.finditer(file_in)]

set_ips = set(ip_match)
# TODO: add a report generating function to add information to a CSV etc.
print(set_ips)

