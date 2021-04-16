import codecs
import re

file = codecs.open('3gables.txt', "r", "utf-8")
lt = file.read()
lt1 = lt.strip().replace(':', '').replace('-', '').replace(',', '').replace('=', '').replace('"', '').lower().split('.')
lt1 = [x for x in lt1 if len(x) > 2]
strings = re.findall(r"\S+", lt1[5])
check = " ".join(strings).split(' ')
print(check)
