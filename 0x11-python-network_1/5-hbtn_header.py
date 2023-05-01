#!/usr/bin/python3
'''Takes in a URL, sends a request to the URL & displays the value,
of the X-Request-Id variable in the response header'''

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = argv[1]
    html = get(url)
    print(html.headers.get('X-Request-Id'))
