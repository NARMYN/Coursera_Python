import urllib.request, urllib.parse, urllib.error
import json
import ssl
url = input("Enter the URL: ")
print('Retrieving: ', url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#decoding data
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    info = json.loads(data) #gives parsed data
except:
    info = None
myinfo = info['comments']
#print(myinfo)
print('User count:', len(myinfo))
sum = 0
for item in myinfo:
    my_count = int(item['count'])
    sum = sum + my_count
print('Sum: ', sum)
