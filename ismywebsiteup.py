import http.client

print("Enter Your Url:")
urli = input()

try:
    url = http.client.HTTPConnection(urli)
    url.connect()
    print ("Site Respond :)")
except:
    print ("Site Didn't Respond :(")
