#!/usr/bin/python3

import argparse
from faker import Faker
import requests
from random import randint

faker = Faker()

def post_goods(address, qty):
    
    for i in range(qty):
        try:
            good = faker.word()
            price = randint(5, 50)

            resp = requests.post(
                address,
                json=[{'good': good,
                    'price': price}]
                    )
        except:
            print('ConnectionError')


def args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-a', '--address', dest='address', action='store', default='http://127.0.0.1:5000/goods',
                         help='receives http address like "http://..."')
    parser.add_argument('-q', '--quantity', dest='quantity', action='store', default=1,
                         type=int, help='receives integer')
    args = parser.parse_args()

    return args



if __name__ == '__main__':
    args = args()
    post_goods(args.address, args.quantity)
