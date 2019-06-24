#examples of using the urllib module in python
#6/24/2019

import urllib
from urllib import request

resp = request.urlopen("https://www.wikipedia.org")

print("HTTP Status code: ",resp.code)
"""
    HTTP Status Codes
    200: OK
    400: Bad Request
    403: Forbidden
    404: Not Found
"""

print("Length of request in bytes: ",resp.length)
print("A peek at the response is: ", resp.peek())

data = resp.read()
print("Our response type is: ", type(data))
print("The length of the data is: ", len(data))

html = data.decode("UTF-8")
print("After decoding the data the type is: ", type(html))
#print(html)  This will print all of the HTML to the console

#The next line demonstrates in the console a 403 error
#resp2 = request.urlopen("https://www.google.com/search?q=socratica")

from urllib import parse
params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
print("Query string: ", querystring)
url = "https://www.youtube.come/watch" + "?" + querystring
resp3 = request.urlopen(url)
print("Response closed?: ", resp3.isclosed())
print("Response code: ", resp3.code)
html = resp3.read().decode("utf-8")

num = 500

print("The first ", num, " characters of ", url, " are: ", html[:500])
