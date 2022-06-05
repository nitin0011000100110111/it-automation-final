#!/usr/bin/env python3

import os
import requests
import json

def generate_json_data(files):
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

def upload_desc(data, url):
    for item in data:
        try:
            r = requests.post(url, item)
        except Exception as e:
            print(f"Error: {e}", f"Status code: {r.status_code}", sep='\n')

def main():
    url = 'http://104.155.136.80/fruits/'
    file = './supplier-data/descriptions/'
    data = generate_json_data(file)
    upload_desc(data=data, url=url)

if __name__ == '__main__':
    main()