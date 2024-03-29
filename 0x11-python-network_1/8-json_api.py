#!/usr/bin/python3
'''Takes in a letter & sends a POST request to,
http://0.0.0.0:5000/search_user with the letter as a parameter'''

if __name__ == "__main__":
    from requests import post
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    if (len(argv) > 1):
        letter = {'q': argv[1]}
    else:
        letter = {'q': ""}
    html = post(url, data=letter)
    try:
        json = html.json()
        if json == {}:
            print('No result')
        else:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
    except ValueError:
        print('Not a valid JSON')
