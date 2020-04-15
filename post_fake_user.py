#!/usr/bin/python

import argparse
from faker import Faker
import requests

faker = Faker()

def post_name(address, qty):  
    for i in range(qty):
        name = faker.name()
        try:
            resp = requests.post(
                address,
                json={'name': name}
            )
        except ConnectionRefusedError:
            print('ConnectionError')


def args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-a', '--address', dest='address', action='store', default='http://127.0.0.1:5000/users', help='receives http address like "http://..."')
    parser.add_argument('-q', '--quantity', dest='quantity', action='store', default=1, type=int, help='receives integer')
    args = parser.parse_args()

    return args



if __name__ == '__main__':
    args = args()
    post_name(args.address, args.quantity)
