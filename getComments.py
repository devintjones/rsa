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


def getComments(call):
	for item in call:
			item["data"]


#getComments(returnjson)



second_dict = returnjson[1]




#2nd one is bigger
insidesecond = second_dict["data"]




#within children within the 2nd object
children = insidesecond["children"]
s = json.dumps(children, sort_keys=True, indent=4 * ' ')
print s

#this doesn't write how it prints
with open('samplejson.txt','w') as outfile:
	json.dump(s,outfile)


first_child = children[0]
f_child_data = first_child["data"]
#for i in f_child_data:
#	print i



#there exists another dict
children_first_dict = children[0]

#for key in children_first_dict:
#	print "key is", key

#prints "t1" what is that?
#print(children_first_dict["kind"])

#comments seem to be here
data = children_first_dict["data"]
#print type(data)

#pretty print
s = json.dumps(data, sort_keys=True, indent=4 * ' ')
#print s
#print '\n'.join([l.rstrip() for l in  s.splitlines()])


#print data["body"]

#this is type 'unicode'
#insidesecond["modhash"]

#this is a list
#insidesecond["children"]