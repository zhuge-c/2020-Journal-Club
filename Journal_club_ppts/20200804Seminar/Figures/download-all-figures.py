#/usr/bin/python3

import requests
import os
import time

url0='https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-020-16904-3/MediaObjects/41467_2020_16904_Fig{}_HTML.png'
for i in range(1,6):
    url=url0.format(i)
    r=requests.get(url)
    print(i,r.status_code)
    with open(os.path.join(os.path.realpath(os.path.dirname(__file__)),'Fig-{}.png'.format(i)),'wb') as fo:
        fo.write(r.content)
    time.sleep(1)