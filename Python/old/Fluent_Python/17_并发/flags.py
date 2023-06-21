import os
import time
import sys

import requests

BASE_URL = 'https://www.pexels.com/zh-cn/photo/'
DOWNLOAD_PATH = 'download/'
Photos = ('906018', '2171077', '2539395', '2929139', '1727200')


def save_photo(img, filename):
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)

    with open(DOWNLOAD_PATH+filename+'.jpg', 'wb') as f:
        f.write(img)

    print(f.name)


def get_photo(photo):
    url = BASE_URL + photo + '/'
    res = requests.get(url)
    
    return res.content


def download_many(photo_list):
    for photo in photo_list:
        image = get_photo(photo)        
        save_photo(image, photo)


def main(download_many):
    t0 = time.time()
    download_many(Photos)
    t1 = time.time()
    
    msg = "耗时 {}".format(t1-t0)
    print(msg)


if __name__ == "__main__":
    main(download_many)