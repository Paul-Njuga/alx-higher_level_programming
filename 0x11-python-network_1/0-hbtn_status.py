#!/usr/bin/python3
'''Fetches https://alx-intranet.hbtn.io/status'''

if __name__ == "__main__":
    from urllib.request import urlopen

    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        html = response.read()
        print(html)
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
