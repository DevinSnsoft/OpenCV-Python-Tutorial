# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 08:30
# @Author  : play4fun
# @File    : compare_photos.py
# @Software: PyCharm

"""
compare_photos.py:
"""

import cv2, pickle
from pprint import pprint

with open('photo_mat', 'rb') as f:
    mat = pickle.load(f)

pairs = []  # 配对好的
lenX = 9  # 行
lenY = 8  # 列


def get_image_difference(image_1, image_2):  # 这个函数不行
    first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
    second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

    img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match

    # taking only 10% of histogram diff, since it's less accurate than template method
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff


def compare(i, j, img):
    for x in range(lenX):
        if x < i:
            continue
        for y in range(lenY):
            if x <= i and y < j:
                continue
            z = mat[x][y]
            # 图片相似度
            y1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            z1 = cv2.cvtColor(z, cv2.COLOR_BGR2GRAY)
            # image_difference = get_image_difference(y1, z1)
            res = cv2.matchTemplate(z1, y1, cv2.TM_CCOEFF_NORMED)
            # print(i, j, x, y, image_difference)
            print(i, j, x, y, res)
            # if abs(image_difference-1)>0.5:
            # if image_difference < 0.1:
            #     pairs.append((i, j, x, y, image_difference))
            if res[0][0] >= 0.8 :#and (i != x and j != y):
                if i ==x and j ==y:
                    continue
                pairs.append((i, j, x, y, res[0][0]))
        print('--------')


for i, x in enumerate(mat):
    for j, y in enumerate(x):
        compare(i, j, y)

print('--------',len(pairs))
pprint(pairs)#156对 #有问题
'''
[(0, 0, 0, 4, 0.81783479),
 (0, 0, 1, 0, 0.82939386),
 (0, 0, 1, 5, 0.80112994),
 (0, 0, 2, 4, 0.81963593),
 (0, 0, 2, 5, 0.80141765),
 (0, 0, 3, 2, 0.83176291),
 (0, 0, 5, 1, 0.82441366),
 (0, 0, 5, 3, 0.93773538),
 (0, 0, 6, 0, 0.80839384),
 (0, 0, 7, 3, 0.80357623),
 (0, 1, 4, 6, 0.84010893),
 (0, 2, 4, 5, 0.89919138),
 (0, 2, 5, 5, 0.89656675),
 (0, 2, 6, 2, 0.87691551),
 (0, 3, 2, 6, 0.94418496),
 (0, 3, 3, 4, 0.97784418),
 (0, 3, 5, 6, 0.91531861),
 (0, 3, 7, 4, 0.90034771),
 (0, 3, 8, 7, 0.8669098),
 (0, 4, 1, 0, 0.95897603),
 (0, 4, 1, 5, 0.9859665),
 (0, 4, 2, 3, 0.84755546),
 (0, 4, 2, 4, 0.98988521),
 (0, 4, 2, 5, 0.97593749),
 (0, 4, 3, 2, 0.96898985),
 (0, 4, 5, 1, 0.93505126),
 (0, 4, 5, 7, 0.92510819),
 (0, 4, 6, 0, 0.88995898),
 (0, 4, 7, 3, 0.91428041),
 (0, 5, 2, 0, 0.90362453),
 (0, 5, 2, 1, 0.93313634),
 (0, 5, 6, 4, 0.88912612),
 (0, 7, 2, 7, 0.98162633),
 (0, 7, 3, 0, 0.84628779),
 (0, 7, 6, 7, 0.85053468),
 (1, 0, 1, 5, 0.93375051),
 (1, 0, 2, 3, 0.80927575),
 (1, 0, 2, 4, 0.95577663),
 (1, 0, 2, 5, 0.93438679),
 (1, 0, 3, 2, 0.98244762),
 (1, 0, 5, 1, 0.95950162),
 (1, 0, 5, 7, 0.9012484),
 (1, 0, 6, 0, 0.93606734),
 (1, 0, 7, 0, 0.81604606),
 (1, 0, 7, 3, 0.91213149),
 (1, 1, 7, 1, 0.8624481),
 (1, 2, 1, 7, 0.94927907),
 (1, 2, 4, 3, 0.97030866),
 (1, 2, 6, 6, 0.89334244),
 (1, 3, 7, 5, 0.90350145),
 (1, 4, 3, 5, 0.92840946),
 (1, 4, 3, 6, 0.92976296),
 (1, 4, 8, 1, 0.87637573),
 (1, 4, 8, 5, 0.86086744),
 (1, 5, 2, 3, 0.83290088),
 (1, 5, 2, 4, 0.98093969),
 (1, 5, 2, 5, 0.9865284),
 (1, 5, 3, 2, 0.95161527),
 (1, 5, 5, 1, 0.91846502),
 (1, 5, 5, 7, 0.93449652),
 (1, 5, 6, 0, 0.87814039),
 (1, 5, 7, 3, 0.91769367),
 (1, 6, 3, 3, 0.87408149),
 (1, 6, 4, 7, 0.83912045),
 (1, 7, 4, 3, 0.93324989),
 (1, 7, 6, 6, 0.90282589),
 (2, 0, 2, 1, 0.98332465),
 (2, 0, 6, 4, 0.89946473),
 (2, 1, 6, 4, 0.91386253),
 (2, 2, 4, 0, 0.97106832),
 (2, 3, 2, 4, 0.85241109),
 (2, 3, 2, 5, 0.84527677),
 (2, 3, 3, 2, 0.83583575),
 (2, 3, 3, 4, 0.80124199),
 (2, 3, 5, 1, 0.81944293),
 (2, 3, 5, 7, 0.819251),
 (2, 3, 7, 0, 0.91440505),
 (2, 3, 7, 3, 0.80969107),
 (2, 4, 2, 5, 0.9853642),
 (2, 4, 3, 2, 0.98278183),
 (2, 4, 5, 1, 0.96176714),
 (2, 4, 5, 3, 0.81060904),
 (2, 4, 5, 7, 0.95080549),
 (2, 4, 6, 0, 0.92093289),
 (2, 4, 7, 0, 0.82010585),
 (2, 4, 7, 3, 0.94900286),
 (2, 5, 3, 2, 0.96413034),
 (2, 5, 5, 1, 0.93163985),
 (2, 5, 5, 3, 0.80133277),
 (2, 5, 5, 7, 0.95228308),
 (2, 5, 6, 0, 0.89228898),
 (2, 5, 7, 0, 0.80005699),
 (2, 5, 7, 3, 0.93504852),
 (2, 6, 3, 4, 0.9634583),
 (2, 6, 5, 6, 0.97281444),
 (2, 6, 7, 4, 0.90955776),
 (2, 6, 8, 6, 0.81169814),
 (2, 6, 8, 7, 0.87542808),
 (2, 7, 3, 0, 0.86373925),
 (2, 7, 6, 7, 0.90865624),
 (3, 0, 6, 7, 0.80371922),
 (3, 1, 3, 7, 0.89857602),
 (3, 2, 5, 1, 0.98385006),
 (3, 2, 5, 3, 0.80837327),
 (3, 2, 5, 7, 0.94026983),
 (3, 2, 6, 0, 0.95155406),
 (3, 2, 7, 0, 0.83519346),
 (3, 2, 7, 3, 0.95594138),
 (3, 3, 4, 7, 0.81548607),
 (3, 3, 8, 4, 0.88165134),
 (3, 4, 5, 6, 0.96190572),
 (3, 4, 7, 4, 0.95597637),
 (3, 4, 8, 7, 0.90763825),
 (3, 5, 3, 6, 0.96791953),
 (3, 5, 7, 7, 0.81160647),
 (3, 5, 8, 5, 0.88941646),
 (3, 6, 7, 7, 0.8219896),
 (3, 6, 8, 1, 0.80933893),
 (3, 6, 8, 5, 0.92017508),
 (4, 1, 6, 5, 0.8459152),
 (4, 1, 7, 2, 0.95110172),
 (4, 2, 6, 1, 0.95789027),
 (4, 3, 6, 6, 0.95759535),
 (4, 4, 5, 1, 0.80212337),
 (4, 4, 7, 3, 0.80778289),
 (4, 4, 8, 2, 0.92399627),
 (4, 5, 5, 5, 0.98698038),
 (4, 5, 6, 2, 0.91531587),
 (5, 0, 5, 4, 0.95705253),
 (5, 1, 5, 3, 0.81610906),
 (5, 1, 5, 7, 0.93452507),
 (5, 1, 6, 0, 0.98169124),
 (5, 1, 7, 0, 0.84997863),
 (5, 1, 7, 3, 0.97735828),
 (5, 2, 8, 3, 0.96606308),
 (5, 3, 5, 7, 0.80398655),
 (5, 3, 6, 0, 0.80013829),
 (5, 3, 7, 3, 0.82962543),
 (5, 5, 6, 2, 0.91919237),
 (5, 6, 7, 4, 0.96237701),
 (5, 6, 7, 6, 0.80884886),
 (5, 6, 8, 6, 0.80175209),
 (5, 6, 8, 7, 0.92764288),
 (5, 7, 6, 0, 0.90893477),
 (5, 7, 7, 0, 0.82358778),
 (5, 7, 7, 3, 0.94626212),
 (6, 0, 7, 0, 0.85159588),
 (6, 0, 7, 3, 0.96886152),
 (6, 3, 8, 0, 0.94173014),
 (6, 5, 7, 2, 0.90841216),
 (7, 0, 7, 3, 0.84417427),
 (7, 4, 8, 7, 0.93397516),
 (7, 6, 8, 6, 0.96749038),
 (7, 7, 8, 1, 0.80834168),
 (7, 7, 8, 5, 0.84336907),
 (8, 1, 8, 5, 0.89013624)]
'''

'''
#Test
# 1, 0, 1, 5
a = mat[1][0]
b = mat[1][5]
y1 = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
z1 = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
# image_difference = get_image_difference(y1, z1)
res = cv2.matchTemplate(z1, y1, cv2.TM_CCOEFF_NORMED)
print(1, 0, 1, 5, res)
'''


def compare_2(x1, y1, x2, y2):
    a = mat[x1][y1]
    b = mat[x2][y2]
    c1 = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    c2 = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    # image_difference = get_image_difference(y1, z1)
    res = cv2.matchTemplate(c2, c1, cv2.TM_CCOEFF_NORMED)
    print(x1, y1, x2, y2, res)


# compare_2(2, 0, 2, 1)
