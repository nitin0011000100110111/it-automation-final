#!/usr/bin/env python3

import os
from PIL import Image
from multiprocessing import Pool

def convert_image(file_path):
    new_file = file_path.replace('.tiff', '.jpeg')
    with Image.open(file_path, 'r') as im:
        im = im.convert('RGB').resize((600, 400))
        im.save(new_file, format='JPEG')
        im.close()

def run(data):
   convert_image(data)

def main():
    data = []
    directory ='./supplier-data/images/'
    for file in os.listdir(directory):
        if file.endswith('.tiff'):
            file_path = os.path.join(directory, file)
            data.append(file_path)
    pool = Pool(len(data))
    pool.map(run, data)

if __name__ == "__main__":
    main()