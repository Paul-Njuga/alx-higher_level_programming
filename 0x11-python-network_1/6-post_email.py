#!/usr/bin/python3
'''Takes in a URL & an email, sends a POST request to the URL,
with the email as a parameter, & displays the response body'''

if __name__ == "__main__":
    from requests import post
    from sys import argv

    url = argv[1]
    email = {'email': argv[2]}
    html = post(url, data=email)
    print(html.text)
