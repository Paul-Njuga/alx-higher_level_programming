#!/usr/bin/python3
'''Takes in a URL & an email, sends a POST request to the URL,
with the email as a parameter, & displays the body,
of the response (decoded in utf-8)'''

if __name__ == "__main__":
    from sys import argv
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

    url = argv[1]
    email = argv[2]
    value = {'email': email}
    data = urlencode(value)
    data = data.encode('ascii')  # Bytes
    req = Request(url, data)
    with urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
