#!/usr/bin/python3

import argparse
from faker import Faker
import requests
from random import randint

faker = Faker()

def post_stores(address, qty):

    for i in range(qty):
        lstore_name = faker.words(2)
        city = fake.city()
        user_id = randint(1, 10)
        try:
            resp = requests.post(address,
                            json=[{'name': f'{lstore_name[0]} {lstore_name[1]}',
                                    'location': city,
                                    'manager_id': user_id}]
                                ) 
        except:
            print('ConnctionError')

def args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-a', '--address', dest='address', action='store', default='http://127.0.0.1:5000/store', help='receives http address like "http://..."')
    parser.add_argument('-q', '--quantity', dest='quantity', action='store', default=1, type=int, help='receives integer')
    args = parser.parse_args()

    return args



if __name__ == '__main__':
    args = args()
    post_goods(args.address, args.quantity)
