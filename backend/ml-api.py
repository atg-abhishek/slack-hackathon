import requests
import simplejson as json 
from utilities import * 
from pprint import pprint

'''

DEPRECATED : removing this because it doesn't work well, see the indico implementation

'''

auth_token = key_fetcher('monkey_learn_api_key')
def get_keywords(data):
	url = 'https://api.monkeylearn.com/v2/extractors/ex_y7BPYzNG/extract/?sandbox=1'
	headers = {"Authorization" : "Token " + auth_token}
	payload = {"text_list" : ['hello how are things going? this is a good day to get started with the project']} 
	r = requests.post(url, headers=headers, data=payload) #data needs to be a python list 
	pprint(r.text)

get_keywords(["hello how are things going? this is a good day to get started with the project", "Shall we go forward with constructing the fastest route to access files from the internet?"])