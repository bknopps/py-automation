import re
import socket
from dns import resolver
import paramiko

# TODO: read from live ASA's
# TODO: import other sources of data.
file = 'C:\\Scripts\\int_fw.txt'

host_object = re.compile('^object network\s(\S+)(?:\n|\r)^\s(host)\s(.+)$', re.MULTILINE)

nat_object = re.compile('^object network\s(\S+)(?:\n|\r)^\s(nat)\s\S+\sstatic\s(\S+)$', re.MULTILINE)


f_in = open(file, 'r')
f_in = f_in.read()
host_matches = [{m.group(2):[m.group(1),m.group(3)]} for m in host_object.finditer(f_in)]
nat_matches = [{m.group(2):[m.group(1),m.group(3)]} for m in nat_object.finditer(f_in)]
print(host_matches)
print(nat_matches)


for i_address in host_matches:
    inside = i_address['host'][0]
    for n_address in nat_matches:
        outside = n_address['nat'][0]
        if inside == outside:
            line = 'Public Address {} NATS to {} labeled {}'.format(n_address['nat'][1], i_address['host'][1], inside)
            try:
                dns_record = socket.gethostbyaddr(i_address['host'][1])
                hostname = dns_record[0]
                line = line + '\t\t Hostname is {}'.format(hostname)
                if len(dns_record[1]) > 0:
                    alias = dns_record[1]
                    line = line + ' , Alias are: {}'.format(alias)

            except:
                pass
            print(line)



