#!/usr/bin/python3
'''Takes your GitHub credentials (username and password),
& uses the GitHub API to display your id'''

if __name__ == "__main__":
    from requests import get
    from sys import argv

    usrnm = argv[1]
    pswd = argv[2]
    headers = {'Authorization': 'token '+pswd}
    req = get('https://api.github.com/users/{}'.format(usrnm), headers=headers)
    print(req.json().get('id'))
