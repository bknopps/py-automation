# Written by: Brad Knopps
# update on 5/22/17
#

import ipaddress
import re


def main():
    '''This is meant to be used on Standard outbound ACL's re-directing for WCCP. Once all overlapping ACL's have been
    removed the ACL is re-written back to a text file.'''
    # TODO: Add support for other version of ACL's (extended, etc..)
    # TODO: Add feature for combining multiple lines into subnets.

    holder_box = []
    raw_acl = importacl(r'c:\scripts\access_list.txt')
    output_acl(raw_acl.pop(0))
    holder_box.append(raw_acl.pop(-1))
    scrubed_acl =[]
    for line in raw_acl:
        ip_search = re.sub('\s+\d+\sdeny\sip\sany\s', '', line)
        scrubed_acl.append(ip_search)
    for line in scrubed_acl:
        if line.endswith('/32') is False:
            match = re.match('\d+\.\d+\.\d+\.\d+/\d+',line)
            if match:
                n1 = ipaddress.IPv4Network(line)
                for n, address in enumerate(scrubed_acl):
                    match = re.match('\d+\.\d+\.\d+\.\d+/\d+', address)
                    if match:
                        n2 = ipaddress.IPv4Network(address)
                        if n1 == n2:
                            pass
                        elif n1.overlaps(n2):
                            print("{} is a Shadown subnet of: {} - removing it from the ACL".format(n2, n1))
                            scrubed_acl.pop(n)

    for item in scrubed_acl:
        output_acl('deny ip any {}\n'.format(item))
    for item in holder_box:
        print(item)
        item = re.sub('^\s+\d+\s', '', item, re.MULTILINE)
        output_acl(item+'\n')


def output_acl(line):
    file = open(r'c:\scripts\new_access_list.txt', 'a+')
    file.write(line)
    file.close()


def importacl(path):
    with open(path, 'r') as f_in:
        acl = f_in.read()
        acl = acl.split('\n')
    return acl


if __name__ == '__main__':
    main()
    