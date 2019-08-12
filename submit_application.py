import os
import argparse

import requests


BASE_URL = os.environ.get('BASE_URL')
BCG_DV_API = f'{BASE_URL}/api/v1'


def get_key():
    r = requests.get(f'{BCG_DV_API}/key')
    return r.json().get('key')


def submit(name: str, email: str):
    data = {'name': name, 'email': email}
    params = {'apiKey': get_key()}

    r = requests.post(f'{BCG_DV_API}/submit', json=data, params=params)
    if (r.status_code == 202):
        print('Submission successful.')
    print(r.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Provide name and email.')
    parser.add_argument('-n', '--name', required=True, help="Full name")
    parser.add_argument('-e', '--email', required=True, help="Email address")
    args = vars(parser.parse_args())

    submit(**args)
