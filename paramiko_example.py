# Written by Bradley Knopps
# Written in Python 3.4
# Written on 3/3/17
import paramiko
import time


user = ''
password = ''
host = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto accept SSH Keys
ssh.connect(host, username=user,
            password=password,
            look_for_keys=False,
            allow_agent=False)
conn = ssh.invoke_shell()  # Use invoke_shell to pass multiple SSH Commands to a shell without having it close.
output = conn.recv(5000)
# the number is the amount of bytes your connection will bring back from stdrout increase to see more data
print(output)
# begin sending commands
conn.send('ls\n')  # command must end with a return character
time.sleep(.5)
# give time for your shell to print to stdrout -
# increase time if your not seeing all your data for longer running commands
output = conn.recv(5000)
print(output)
