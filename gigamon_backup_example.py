import paramiko
import time
import re
import getpass

ips = ['10.10.10.10', '10.10.10.10']
user=input('Enter Username: ')
password = getpass.getpass('Enter Password')


for host in ips:
    #Paramiko makes SSH Connections to devices
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Auto accept SSH Keys
    ssh.connect(host, username=user,
                password=password,
                look_for_keys=False,
                allow_agent=False)
    conn = ssh.invoke_shell() #Use invoke_shell to pass multiple SSH Commands to a shell without having it close.
    time.sleep(1)
    output = conn.recv(500)
    #print(output)
    conn.send('\n')
    time.sleep(1)
    output = conn.recv(500)
    #print(output)
    conn.send('enable\n')
    time.sleep(1)
    output = conn.recv(500)
    #print(output)
    conn.send('terminal length 999\n')
    time.sleep(1)
    output = conn.recv(999)
    conn.send('show run\n')
    time.sleep(15)
    run_output = conn.recv(999995)
    str_output = str(run_output, 'utf-8')
    #print(run_output)
    #Change File path to folder you wish to hold backup.
    f_out = open('c:\\data\\{}.txt'.format(host), 'w') # opens file with hostname
    print('writing the version and running-config output to file {}.txt'.format(host))
    f_out.write(str_output) #write output
    f_out.close() #close file

