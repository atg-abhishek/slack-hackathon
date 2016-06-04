import requests
from pprint import pprint 
import simplejson as json 
from utilities import * 

'''

can't use this because you have to provide credit card to even access the free APIs

'''

api_key = key_fetcher("mashape_ontology_api_key")
def get_categories(text=""):
	url = "https://proxem-thematization.p.mashape.com/api/wikiAnnotator/GetCategories?nbtopcat=20"
	headers = {'X-Mashape-Key' : api_key, "Accept" : "application/json", "Content-Type" : "text/plain"}
	r = requests.post(url, headers=headers, data=text)
	pprint(r.text)

get_categories("The National Aeronautics and Space Administration (NASA) is an independent agency of the executive branch of the United States Federal Government responsible for the civilian space program as well as aeronautics and aerospace research.")