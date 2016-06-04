import requests
from pprint import pprint 
import simplejson as json 
from utilities import *

api_key = key_fetcher('indico_api_key')
def get_keywords(sentence=""):
	url = "https://apiv2.indico.io/keywords?key="+api_key+"&version=2"
	r = requests.post(url, data={"data" : "The National Aeronautics and Space Administration (NASA) is an independent agency of the executive branch of the United States Federal Government responsible for the civilian space program as well as aeronautics and aerospace research."})
	pprint(r.text)

def get_sentiments(sentence=""):
	url = "https://apiv2.indico.io/sentimenthq?key="+api_key
	r = requests.post(url, data={"data": "They seriously need to fix the IT equipment, the printer has made me waste so much time"})
	pprint(r.text)

get_sentiments()