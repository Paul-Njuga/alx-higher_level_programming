#!/usr/bin/python3
'''Takes in a URL, sends a request to the URL & displays,
the body of the response (decoded in utf-8)'''

if __name__ == "__main__":
    from sys import argv
    from urllib.error import HTTPError
    from urllib.request import Request, urlopen

    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
