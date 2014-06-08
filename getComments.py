import requests
import simplejson as json



def sendCall(matchquery): #sends api call and returns json as python dict
	formatquery = matchquery.replace(" ", "+")
	#build api query
	urlbase = 'https://ws.spotify.com/search/1/track.json?q=' 
	call = urlbase + formatquery
	
	call = requests.get(call) #send call
	returnjson = call.json() #turn api response into a python dict
	return returnjson


url = 'http://www.reddit.com/r/mildlyinteresting/comments/27m9t7/this_bar_requires_you_to_be_23_to_enter/'

call = requests.get(url) #send call

returnjson  = call.json()

print returnjson