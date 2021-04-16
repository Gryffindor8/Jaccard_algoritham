import codecs
import operator
import os
import re
from os import walk
from numpy import mean


def jaccardIndex(x, y):
    intersection = len(list(set(x).intersection((set(y)))))
    union = len(list(set(x).union((set(y)))))
    return intersection / union
    # intersection = len(list(set(list1).intersection(list2)))
    # union = (len(list1) + len(list2)) - intersection
    # return float(intersection) / union


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avgg = sum_num / len(num)
    return avgg


path = os.getcwd()
dict1 = {}
avg = []
sort = []
file = []
maxi = []
_, _, filenames = next(walk(path + "\\Stories"))
i = 0
name = ""
query = "good day"
query = query.lower().replace(",", " ").strip().split(' ')
for f in filenames:
    file = codecs.open(path + "\\Stories\\" + f, "r", "utf-8")
    try:
        # file = codecs.open('3gables.txt', "r", "utf-8")
        lt = file.read()
        lt1 = lt.strip().replace(':', '').replace('-', '').replace(',', '').replace('=', '').replace('"',
                                                                                                     '').lower().split(
            '.')
        lt1 = [x for x in lt1 if len(x) > 2]
        for k in lt1:
            strings = re.findall(r"\S+", k)
            check = " ".join(strings).split(' ')
            o = jaccardIndex(query, check)
            if o > 0.1:
                avg.append(o)
        thresh = (mean(avg))
        if thresh > 0.1936:
            dict1[thresh] = f
    except ValueError:
        i = i + 1
        name = f
        print((i, f))
sorted_x = sorted(dict1.items(), key=operator.itemgetter(0))
print("Top 5 books with their Most similarity inddex:", sorted_x[-5:])
print("Total Matched Books:", len(sorted_x))
print(sorted_x)
