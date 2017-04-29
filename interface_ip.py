import re

# supply file with file path to a show run of your NXOS device
file = 'C:\\Scripts\\showrun.txt'

# gather interface ip address
host_object = re.compile('^\s+ip\saddress\s(\d+\.\d+\.\d+\.\d+)', re.MULTILINE)
# gather HSRP interface addresses
hsrp_object = re.compile('^\s+ip\s(\d+\.\d+\.\d+\.\d+)', re.MULTILINE)

file_in = open(file, 'r')
file_in = file_in.read()
# create list of IP's
ip_match = [m.group(1) for m in host_object.finditer(file_in)]
hsrp_match = [m.group(1) for m in hsrp_object.finditer(file_in)]
# merge and sort IP's
merged_ips = ip_match + hsrp_match
print(sorted(merged_ips))

