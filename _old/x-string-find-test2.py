try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
html = '''<html>
<head>Heading</head>
<body attr1='val1'>
    <div class='container'>
        <div id='class'>Something here</div>
        <div>Something else</div>
    </div>
</body>
</html>'''#the HTML code you've written above

inTxt = 'chipotle_html/chipotlepage.html'

with open(inTxt, 'r') as myfile:
    data=myfile.read().replace('\n', '')


parsed_html = BeautifulSoup(open(inTxt)) #html)

print parsed_html

for i in parsed_

print parsed_html.body.find('div', attrs={'class':"u-block u-pullRight"}).text