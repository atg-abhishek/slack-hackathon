import simplejson as json 
from pprint import pprint
import operator
from collections import defaultdict
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

def execute():
	filenames = ["montreal","newyork", "sanfrancisco", "london"]
	try:
		for filename in filenames:
			pprint(filename)
			x = process(filename)
			total=0
			for item in x:
				total = total + item['val']
			average = total/len(x)
			with open("../datafiles/processed_"+filename+".json",'w') as outfile:
				json.dump({"data": x, "average" : average}, outfile)
		return "success"
	except:
		return "failed"

def keyword_cloud():
	filenames = ["montreal","newyork", "sanfrancisco", "london"]
	d = defaultdict(list)
	for f in filenames:
		temp = {}
		pprint(f)
		with open('../datafiles/processed_'+f+'.json') as infile:
			temp = json.load(infile)
		data = temp['data']
		for x in data: 
			kws = x['keywords']
			for k in kws:
				d[k[0]].append(k[1])
	result = []
	for a,b in d.items():
		result.append([a, len(b) ])
	return result

def generate_word_cloud():
	x = keyword_cloud()
	xy = sorted(x, key=operator.itemgetter(1), reverse=True)
	f = open('output.txt','w')
	for a in xy:
		f.write(a[0]*a[1])
		f.write("\n")	

# def pre_char

# def generate_chart_data(city):
# 	with open('')
