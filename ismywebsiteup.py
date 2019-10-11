import http.client

print("Enter Your Url:")
urli = input()

try:
    url = http.client.HTTPConnection(urli)
    url.connect()
    print ("Site Respond :)")
    input('Press any key to exit')
except:
    print ("Site Didn't Respond :(")
    input('Press any key to exit')
