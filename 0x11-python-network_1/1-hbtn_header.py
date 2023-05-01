#!/usr/bin/python3
'''Takes in a URL, sends a request to the URL & displays the value,
of the X-Request-Id variable found in the header of the response'''

if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen

    url = argv[1]
    with urlopen(url) as response:
        html = response.read()
        # get doesn't throw an exception if key doesn’t exist
        print(response.headers.get('X-Request-Id'))
