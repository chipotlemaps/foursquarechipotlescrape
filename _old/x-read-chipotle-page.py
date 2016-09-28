inTxt = 'chipotle_html/chipotlepage.html'

with open(inTxt, 'r') as myfile:
    data=myfile.read().replace('\n', '')

print data

import re

preStr = '<img class="u-block u-pullRight" src="http://maps.google.com/maps/api/staticmap?center='

urls = re.findall(r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$', data)
print ', '.join(urls)

import re
foo = "SRID=4326;MULTIPOLYGON(((352877.02163887 1233618.83923531 5,352872.32998848 1233609.44478035 5,352867.693426132 1233612.15611458 5,352861.67354393 1233602.76770592 5,352841.814386368 1233616.9818058 5,352848.495328903 1233625.69463921 5,352861.076768875 1233617.56668663 5,352866.429475784 1233626.28557014 5,352877.02163887 1233618.83923531 5)))"
print re.findall('([\d.]+?)\s([\d.]+?)\s([\d.]+?)', data)

m = re.match("\W*api/staticmap?center[^:]*:=dD*(\d+)", data)

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(open(inTxt))

# #print soup

# for link in soup.find_all('im'):
#     print(link.get('href'))

# def match_class(target):
#     target = target.split()
#     def do_match(tag):
#         try:
#             classes = dict(tag.attrs)["class"]
#         except KeyError:
#             classes = ""
#         classes = classes.split()
#         return all(c in classes for c in target)
#     return do_match

# matches = soup.findAll(match_class("u-block u-pullRight"))
# for m in matches:
#     print m
