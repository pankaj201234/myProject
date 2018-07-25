import json

file = open("TWEET.txt","r")

a = open("count-trump.txt","a")
#b = open("id-trump.txt","a")
#c = open("time_stamp-trump.txt","a")
d = open("text-tweet.txt","a")
#e = open("place-trump.txt","a")
#f = open("user-trump.txt","a")
#g = open("favorite_count-trump.txt","a")
#h = open("retweet_count-trump.txt","a")
#i = open("quote_status-trump.txt","a")
#j = open("retweet_text","w")
'''k = open("retweet_favourite","w")
l = open("retweet_retweet","w")
m = open("retweet_id","w")
n = open("retweet_timestamp","w")'''
count = 1
for lines in file:
	if(count % 2 == 0):
		obj = json.loads(lines)
		s = obj.keys()
		if(("text" in s) and ("place" in s)):
			'''a.write(str(count)+ "\n")
			b.write(str(obj["id"])+ "\n")
			c.write(obj["created_at"]+ "\n")'''
			d.write(obj["text"] + "\n")
			'''e.write(str(obj["place"])+ "\n")
			f.write(str(obj["user"])+ "\n")
			g.write(str(obj["favorite_count"])+ "\n")
			h.write(str(obj["retweet_count"])+ "\n")
			if("quote_status" in s):
				i.write(str(obj[quote_status])+ "\n")
			else:
				i.write("None\n")'''
			'''if("retweeted_status" in s):
				string = obj["retweeted_status"]["text"]
				string = string.rstrip()
				string = string.replace("\n"," ")
				j.write(string + "\n")
				''''''k.write(str(obj["retweeted_status"]["favorite_count"]) + "\n")
				l.write(str(obj["retweeted_status"]["retweet_count"])+ "\n")
				m.write(str(obj["retweeted_status"]["id"]) + "\n") 
				n.write(obj["retweeted_status"]["created_at"]+ "\n")'''
	count = count + 1
