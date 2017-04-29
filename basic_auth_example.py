import base64
import getpass
username = getpass.getuser()
password = getpass.getpass(prompt='Password: ', stream=None)

formatted_pass = '{}:{}'.format(username, password)
basic_auth = base64.b64encode(str.encode(password))
print(basic_auth)
