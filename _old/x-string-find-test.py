from bs4 import BeautifulSoup as bs


c_addr = []
id_addr = []
data = \
"""
<h2>Primary Location</h2>
<div class="address" id="10">
    <p>
       No. 4<br>
       Private Drive,<br>
       Sri Lanka&nbsp;ON&nbsp;&nbsp;K7L LK <br>
"""

inTxt = 'chipotle_html/chipotlepage.html'

with open(inTxt, 'r') as myfile:
    data=myfile.read().replace('\n', '')


soup = bs(data)

for i in soup.find_all('div'):
    # get data using "class" attribute
    addr = ""
    if i.get("class")[0] == u'maps/api/staticmap?center=': # unicode string
        text = i.get_text()
        for line in text.splitlines(): # line-wise
            line = line.strip() # remove whitespace
            addr += line # add to address string
        c_addr.append(addr)
print addr
    # # get data using "id" attribute
    # addr = ""
    # if int(i.get("id")) == 10: # integer
    #     text = i.get_text()
    #     # same processing as above
    #     for line in text.splitlines():
    #         line = line.strip()
    #         addr += line
    #     id_addr.append(addr)

# print "id_addr"
# print id_addr
# print "c_addr"
# print c_addr