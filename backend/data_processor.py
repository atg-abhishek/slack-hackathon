import simplejson as json 
from pprint import pprint
from indico import * 
def process(filename):
	temp = {}
	with open("../datafiles/"+filename+".json") as infile:
		temp = json.load(infile)
	messages = temp['messages']
	res = []
	i=0
	for m in messages:
		text = m['text']
		val = get_sentiments(text)
		emotion = get_emotions(text)
		keywords = get_keywords(text)
		res.append({"text" : text, "val" : val, "emotion" : emotion, "keywords" : keywords})
		pprint(i)
		i = i+1
	return res

filenames = ["montreal","newyork", "sanfrancisco"]
for filename in filenames:
	pprint(filename)
	x = process(filename)
	total=0
	for item in x:
		total = total + item['val']
	average = total/len(x)
	with open("../datafiles/processed_"+filename+".json",'w') as outfile:
		json.dump({"data": x, "average" : average}, outfile)