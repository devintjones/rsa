import requests
import simplejson as json
import csv




url = 'http://www.reddit.com/r/gifs/comments/27zd5r/did_you_see_that_how/.json'

call = requests.get(url) #send call

#in the comments page, this has 2 dicts. 
#1st is the thing being commented on
#2nd is all of the comments
returnjson  = call.json()

#pretty print
#s = json.dumps(returnjson[0], sort_keys=True, indent=4 * ' ')
#print '\n'.join([l.rstrip() for l in  s.splitlines()])



def getRedditComments(call):
	comments = []
	if call["data"]["children"]:
		children = call["data"]["children"]
		for child in children:
			if child["data"]:
				comments.append([child["data"]["body"]])
				if child["data"]["replies"]:
					getRedditComments(child["data"]["replies"])
					print '1'	
	return comments

comments = getRedditComments(returnjson[1])

print comments


with open('reddit_comments.csv','wb') as f:
	writer = csv.writer(f)
	for comment in comments:
		writer.writerows([comment])
