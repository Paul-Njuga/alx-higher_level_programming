#!/usr/bin/python3
'''Fetches https://alx-intranet.hbtn.io/status'''

if __name__ == "__main__":
    from requests import get

    html = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(html.text)))
    print('\t- content: {}'.format(html.text))
