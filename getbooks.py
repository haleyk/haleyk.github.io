import requests
from bs4 import BeautifulSoup
import requests
import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import colorsys

def get_dom_col(url):
    pixels = np.float32(io.imread(url).reshape(-1, 3))
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)] # 3 element color
    return dominant


webs = 'https://www.goodreads.com/user/year_in_books/2021/126421221'
page = requests.get(webs)
code = page.status_code
if code == 200: soup = BeautifulSoup(page.content, 'html.parser')


n_colors = 10
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
flags = cv2.KMEANS_RANDOM_CENTERS

books = {}
for item in [x for x in soup.find_all('img')]:
    try: t = item['title']; im = item['src']; books[t] = im
    except: haley=1


colours = []
for t,i in books.items():
    print(len(colours))
    colours.append((t, np.uint8(get_dom_col(i))/255))
colours.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb[1]))
colours_copy = colours.copy()

# haven't decided if the orfering. but okay.

books_copy = list(books.items())
for ix in range(10):
    print('books'+str(ix+1)+':')
    for x in range(10):
        t,cl = colours_copy.pop(); i=books[t]
        print("- {title: \""+t+"\", cover: \""+i+"\"}")
    print()









# eof
