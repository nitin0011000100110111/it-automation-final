#!/usr/bin/env python3
import os
import requests

def upload(url, image_dir):
    for file in os.listdir(image_dir):
        if file.endswith('.jpeg'):
            with open(image_dir + file, 'rb') as opened:
                try:
                    r = requests.post(url, files={'file': opened})
                    if r.status_code == '200':
                        print('Image {file} uploaded.')
                except Exception as e:
                    print(e)

def main():
    url = 'http://localhost/upload/'
    image_dir = './supplier-data/images/'
    upload(url, image_dir)

if __name__ == '__main__':
    main()