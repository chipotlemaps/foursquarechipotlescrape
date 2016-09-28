import urllib, json
import pandas as pd 
import time
from _secret_info import client_id, client_secret

inCSV = 'data/input/locations/chipotle_locations.csv'

df = pd.read_csv(inCSV)

theDate = (time.strftime("%Y%m%d"))

def getFoursquareVenueID(clientSecret,clientID,latitude,longitude,venueName,theDate):
    theUrl = 'https://api.foursquare.com/v2/venues/search?ll='+str(latitude)+','+str(longitude)+'&client_id='+clientID+'&client_secret='+clientSecret+'&v='+theDate
    print theUrl
    response = urllib.urlopen(theUrl)
    data = json.loads(response.read())
    venues = data["response"]["venues"]
    for i in venues:
		if i["name"] == venueName:
			#print i['id'], i['stats']['checkinsCount'], i['stats']['tipCount'], i['stats']['usersCount']
			#return i['id'], i['stats']['checkinsCount'], i['stats']['tipCount'], i['stats']['usersCount']
			return i['id']
    time.sleep(1)

#df['venue_id'], df['checkinsCount'], df['tipCount'], df['usersCount'] = zip(*df.apply(lambda row: getFoursquareVenueID(client_secret,client_id,row['latitude'], row['longitude'],"Chipotle Mexican Grill",theDate), axis=1))
df['venue_id'] = df.apply(lambda row: getFoursquareVenueID(client_secret,client_id,row['latitude'], row['longitude'],"Chipotle Mexican Grill",theDate), axis=1)

ouCSV = 'data/processing/chipotle_locations_with_venue_id.csv'
df.to_csv(ouCSV,index=False)


