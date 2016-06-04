import simplejson as json

def key_fetcher(name):
        with open('keys.json') as infile:
                res = json.load(infile)
        return res[name]
