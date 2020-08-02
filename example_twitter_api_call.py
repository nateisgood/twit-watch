#%%
"""
twitter example api cells 

@author: nate
"""

#%%
import twitter
import json

def load_creds():
    with open('creds.json', 'r') as file:
        creds = json.load(file)
    
    return creds

creds = load_creds()

#%%
api = twitter.Api(consumer_key=creds['consumer_key'],
                  consumer_secret=creds['consumer_secret'],
                  access_token_key=creds['access_token_key'],
                  access_token_secret=creds['access_token_secret'])

#%%
results = api.GetSearch('Honeywell')


# %%
