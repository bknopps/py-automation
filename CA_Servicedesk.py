import requests
import base64
import getpass
import re
# This script is a working example of how to open a change order in CA Service Desk.


username = ''
password = getpass.getpass(prompt='Password: ', stream=None)

# formatted to username:password for base64 encoding
formatted_pass = '{}:{}'.format(username, password)
# base64 encoding is required for basic auth (Note: will be return as bytes object)
basic_auth = base64.b64encode(str.encode(formatted_pass))
# decoding from bytes to string literal
basic_auth = bytes.decode(basic_auth)
#print(basic_auth)

url = "http://your-servicedesk:8050/caisd-rest/rest_access"
#this XML tag MUST be sent in the body of the POST request to recieve token
payload = "<rest_access/>"
headers = {
    'authorization': "Basic {}".format(basic_auth),
    'content-type': "application/xml",
    'cache-control': "no-cache"
    } #Header must be set to 'application/xml'

response = requests.request("POST", url, data=payload, headers=headers) # you need to do a POST to get the X-AccessKey

"""we want the access_key - this will be put into the header our following API calls as X-AccessKey"""
output = response.text
print(output)
access_key = re.compile('<access_key>(\d*)</access_key>')
m = access_key.search(output)
key = m.group(1)


# change post is the xml needed to post a change request.
#  you will need to do some research to find our what values are relevant to your group in CA Servicedesk.
change_post = """
<chg>
    <summary></summary>
    <affected_contact COMMON_NAME=""/>
    <assignee COMMON_NAME=""/>
    <backout_plan></backout_plan>
    <business_case></business_case>
    <category COMMON_NAME="Infrastructure Configuration"/>
    <chgtype COMMON_NAME="Standard"/>
    <description></description>
    <effort></effort>
    <group COMMON_NAME="Network Engineering"/>
    <impact COMMON_NAME="None"/>
    <priority COMMON_NAME="None"/>
    <requestor COMMON_NAME=""/>
    <sched_start_date></sched_start_date>
    <zaffected_company REL_ATTR="number here"/>
    <zbusiness_reason COMMON_NAME="string here"/>
    <zpeer_approval COMMON_NAME="No"/>
</chg>"""

change_url = "http://your-servicedesk:8050/caisd-rest/chg"

change_headers = {
    'authorization': "Basic {}".format(basic_auth),
    'X-AccessKey': key,
    'content-type': "application/xml"
    }

response = requests.request("POST", change_url, data=change_post, headers=change_headers)
print(response.text)


