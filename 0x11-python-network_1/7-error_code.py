#!/usr/bin/python3
'''Takes in a URL, sends a request to the URL,
& displays the response body'''

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = argv[1]
    html = get(url)
    if (html.status_code >= 400):
        print('Error code: {}'.format(html.status_code))
    else:
        print(html.text)
