import requests
from bs4 import BeautifulSoup
import requests
import cv2
import numpy as np
import pandas as pd
from skimage import io
import matplotlib.pyplot as plt
import colorsys

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }


df = pd.read_csv('goodreads_library_export24.csv')
books = {}; books5s = {}
for year in ['2020','2021','2022','2023','2024']:
    webs = 'https://www.goodreads.com/user/year_in_books/'+year+'/126421221'
    page = se.get(webs)
    code = page.status_code
    if code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
    for item in [x for x in soup.find_all('img')]:
        try:
            t = item['title']; im = item['src']
            books[t] = im
            tit,auth = t.split(' by ')
            stars = df.loc[(df.Title.str.contains(tit))&(df.Author==auth)]['My Rating'].values[0]
            num = df.loc[(df.Title.str.contains(tit))&(df.Author==auth)]['Book Id'].values[0]
            if stars==5:
                books5s[t] = (im,num)
        except:
            haley=1
# this new version just prints them all in one group to be randomized
print('books:')
for t,ii in books5s.items():
    i = ii[0]
    n = str(ii[1])
    print("- {title: \""+t+"\", id: \""+n+"\", cover: \""+i+"\"}\n")
# write this to a file called books.yml which should go in _data
with open("_data/books.yml", "w") as bfile:
    # Writing data to a file
    bfile.write("books:\n")
    for t,ii in books5s.items():
        i = ii[0]
        n = str(ii[1])
        bfile.write("- {title: \""+t+"\", id: \""+n+"\", cover: \""+i+"\"}\n")


# https://www.goodreads.com/book/show/186074





# def get_dom_col(url):
#     pixels = np.float32(io.imread(url).reshape(-1, 3))
#     _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
#     _, counts = np.unique(labels, return_counts=True)
#     dominant = palette[np.argmax(counts)] # 3 element color
#     return dominant


# books = {}
# for year in ['2021','2022','2023']:
#     webs = 'https://www.goodreads.com/user/year_in_books/'+year+'/126421221'
#     page = requests.get(webs)
#     code = page.status_code
#     if code == 200: soup = BeautifulSoup(page.content, 'html.parser')
#     for item in [x for x in soup.find_all('img')]:
#         try: t = item['title']; im = item['src']; books[t] = im
#         except: haley=1

# n_colors = 10
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
# flags = cv2.KMEANS_RANDOM_CENTERS


# colours = []
# for t,i in books.items():
#     print(len(colours))
#     colours.append((t, np.uint8(get_dom_col(i))/255))
# colours.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb[1]))
# colours_copy = colours.copy()

# # haven't decided if the ordering. but okay.

# books_copy = list(books.items())
# for ix in range(10):
#     print('books'+str(ix+1)+':')
#     for x in range(10):
#         t,cl = colours_copy.pop(); i=books[t]
#         print("- {title: \""+t+"\", cover: \""+i+"\"}")
#     print()









# eof
