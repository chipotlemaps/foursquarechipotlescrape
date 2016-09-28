from _secret_info import client_id, client_secret

theDate = '20160913' #YYYYMMDD

print 'https://api.foursquare.com/v2/venues/search?ll=40.7,-74&client_id='+client_id+'&client_secret='+client_secret+'&v='+theDate


print 'https://api.foursquare.com/v2/venues/search?near=new york, ny&categoryId=4d4b7105d754a06374d81259&query=chipotle&limit=50&client_id='+client_id+'&client_secret='+client_secret+'&v='+theDate

print 'https://api.foursquare.com/v2/venues/search?ll=40.7144656,-74.0060888&client_id='+client_id+'&client_secret='+client_secret+'&v='+theDate
