#!/usr/bin/env python3
import os
import requests
import json
from multiprocessing import Pool


def gen_json(files):
    data = []
    for file in os.listdir(files):
        filename = file.strip('.txt')
        keys = ['name', 'weight', 'description', 'image_name']
        values = []
        with open(files + file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line.endswith('lbs'):
                    line = (int(line.strip(' lbs')))
                values.append(line)
            f.close()
            values.insert(3, '.'.join([filename, 'jpeg']))
        data.append(dict(zip(keys, values)))
        data = sorted(data, key=lambda l: l['name'])
    return json.dumps(data)

# def run(data):
#     URL = 'http://[linux-instance-external-IP]/fruits/'
#     response = requests.post(url=URL, data=data)
#     return print(f"{response.status_code}")

# def upload_desc(data):
#     pool = Pool(len(data))
#     pool.map(run, data)
def upload_desc(data, url):
    for item in data:
        r = requests.post(url, item)
        print(f"{r.status_code}", item)

def main():
    url = 'http://104.155.136.80/fruits/'
    file = './supplier-data/descriptions/'
    data = gen_json(file)
    upload_desc(data=data, url=url)

if __name__ == '__main__':
    main()