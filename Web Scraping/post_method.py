import urllib.parse
import urllib.request

#Form URL: http://www.tizag.com/phpT/examples/formexample.php



#URL of CGI script it calls:
url = "http://www.tizag.com/phpT/examples/formexample.php"

values = { 'Fname' : "Jay",
           'Lname' : "Summet",
            'food[]': "Steak",
            "TofD": "Day",
            "submit": "submit"  #This PHP example checks for this entry!
           }

data = urllib.parse.urlencode(values)
data = data.encode('ascii')   #Needed for Python 3.2 and above!
req = urllib.request.Request(url,data)

response = urllib.request.urlopen(req)
the_page = response.read()  #As bytes!
#print(the_page)
pageStr = the_page.decode()         #As a string!

# print(pageStr)

# Find the printed data...
helloAt = pageStr.find("PHP Tutorial")
print("Hello at:", helloAt )
print(pageStr[helloAt:helloAt+300] )