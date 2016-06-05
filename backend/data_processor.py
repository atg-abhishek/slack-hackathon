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

# def pre_chart_data(city):
# 	temp = {}
# 	with open('../datafiles/'+city+".json") as infile:
# 		temp = json.load(infile)
# 	messages = temp['messages']
# 	pprint(messages)
# 	messages = messages[::-1]
# 	ts = []
# 	for m in messages:
# 		ts.append(float(m['ts']))
# 	mintime = min(ts)
# 	maxtime = max(ts)
# 	interval = (maxtime-mintime)/10
# 	# pprint(interval)
# 	block = mintime
# 	chart_data = []
# 	x=0
# 	pprint('entering while blcok')
# 	while(x<len(messages)):
# 		block = block + interval
# 		total = 0
# 		i = 0
# 		while(float(messages[x]['ts'])<block):
# 			pprint(m['text'])
# 			val = get_sentiments(m['text'])
# 			total = total + float(val)
# 			i = i+1
# 			x= x +1
# 			pprint("i " + str(i) )
# 			pprint("x " + str(x))
# 		chart_data.append(total/i)
# 	pprint(chart_data)

def pre_chart_data(city):
	temp = {}
	with open('../datafiles/processed_'+city+'.json') as infile:
		temp = json.load(infile)
	data = temp['data']
	interval = len(data)/10
	chart_data = []
	for i in range(1,11):
		total = 0

		for x in range(0,int(interval+1)):
			total = total + float(data[i+x]['val'])
		chart_data.append(total/interval)

	# pprint(chart_data)
	return chart_data

def sales_data(city):
	
	if city=='montreal':
		return [145555,157341,165420,170132,172998,179564,186004,193321,200012,199922]
	if city=='london':
		return [165555,160361,165420,160767,155398,152564,149304,147111,145042,142333]
	if city=='sanfrancisco':
		return [164555,160361,165420,160767,166398,167564,163304,162111,170042,171333]
	if city=='newyork':
		return [150555,157341,158420,1580132,161998,162564,165004,161321,163412,166922]

# def generate_chart_data(city):
# 	with open('')


# pre_chart_data('montreal')
# pre_chart_data('sanfrancisco')
# pre_chart_data('newyork')