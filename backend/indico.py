import requests
from pprint import pprint 
import simplejson as json 
from utilities import *
import operator

api_key = key_fetcher('indico_api_key')
def get_keywords(sentence=""):
	url = "https://apiv2.indico.io/keywords?key="+api_key+"&version=2"
	try:
		r = requests.post(url, data={"data" : sentence})
		val = r.json()['results']
		sorted_val = sorted(val.items(), key=operator.itemgetter(1), reverse=True)
		res = []
		if (len(sorted_val) > 5):
			res = [sorted_val[0], sorted_val[1], sorted_val[2], sorted_val[3], sorted_val[4]]
		else:
			for sv in sorted_val:
				res.append(sv)
		return res
	except:
		return "null"

def get_sentiments(sentence=""):
	url = "https://apiv2.indico.io/sentimenthq?key="+api_key
	try:
		r = requests.post(url, data={"data" : sentence})
		val = r.json()['results']
		return val
	except:
		return "null"

def get_emotions(sentence=""):
	url = "https://apiv2.indico.io/emotion?key="+api_key
	try:
		r = requests.post(url, data={"data" : sentence})
		# pprint(r.text)
		val = r.json()['results']
		# pprint(type(val))
		sorted_val = sorted(val.items(), key=operator.itemgetter(1), reverse=True)
		res = [sorted_val[0], sorted_val[1]]
		return res
	except:
		return "null"

# x = get_emotions("well this is such an interesting thing, let's talk more about this tomorrow")
# pprint(x)
# pprint(str(x[0][1]) + " " + str(x[1][1]))

# y = get_keywords("Yes, but it's not as good as it was back in the day")
# x = get_keywords("The National Aeronautics and Space Administration (NASA) is an independent agency of the executive branch of the United States Federal Government responsible for the civilian space program as well as aeronautics and aerospace research")
# pprint(y)