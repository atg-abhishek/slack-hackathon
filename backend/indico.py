import requests
from pprint import pprint 
import simplejson as json 
from utilities import *

api_key = key_fetcher('indico_api_key')
def get_keywords(sentence=""):
	url = "https://apiv2.indico.io/keywords?key="+api_key+"&version=2"
	r = requests.post(url, data={"data" : sentence})
	pprint(r.text)

def get_sentiments(sentence=""):
	url = "https://apiv2.indico.io/sentimenthq?key="+api_key
	r = requests.post(url, data={"data": sentence})
	pprint(r.text)

def get_emotion(sentence=""):
	url = "https://apiv2.indico.io/emotion?key="+api_key
	r = requests.post(url, data={"data":sentence})
	pprint(r.text)

