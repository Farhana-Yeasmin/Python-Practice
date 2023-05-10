import urllib.request # Module for reading from the web
import re

"""
Here is the another way to open a url:
=> 
import urllib.request

request = urllib.request.Request("http://www.wsbtv.com/s/weather")
response = urllib.request.urlopen(request)
the_page = response.read()
theText = the_page.decode()
"""

url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"
response = urllib.request.urlopen(url) 
html = response.read() # Gets an array of bytes
htmlStr = html.decode() # convert to a string

phoneNumber = re.findall("\(\d+\) ?\d+-\d+",htmlStr)

for item in phoneNumber:
    print(item)

