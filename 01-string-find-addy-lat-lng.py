import pandas as pd 

inTxt = 'data/input/chipotle_html/chipotlepage.html'

with open(inTxt, 'r') as myfile:
    data=myfile.readlines()#.replace('\n', '')

lat = []
lng = []
addr = []

for i in data:
	if 'http://maps.google.com/maps/api/staticmap?center=' in i:
		latStr = i.split('center=',1)[1].split('%2C',1)[0]
		lngStr = i.split('%2C',1)[1].split('&amp;maptype',1)[0]
		#print latStr, lngStr
		lat.append(latStr)
		lng.append(lngStr)

	if '<a class="location-directions__link link--yellow" href="http://maps.google.com/maps?f=d&amp;source=s_d&amp;daddr=' in i:
		addy = i.split(';daddr=',1)[1].split('" target="_blank"',1)[0].replace('+',' ').replace('%2c',',')
		#print addy
		addr.append(addy)


df = pd.DataFrame({'address' : addr, 'latitude' : lat, 'longitude':lng})

print len(df.index)
print df.head(10)

ouCSV = 'data/input/locations/chipotle_locations.csv'

df.to_csv(ouCSV, index=False)
