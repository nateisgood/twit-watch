#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:09:44 2020

@author: nate
"""
import twitter
import json

def load_creds():
    with open('creds.json', 'r') as file:
        creds = json.load(file)
    
    return creds

creds = load_creds()

api = twitter.Api(**creds)

results = api.GetSearch('Bojack Horseman')


#%%
obj = {
    'consumer_key': 'lEU4diypFEoBnbUg6tVoPOVBz',
    'consumer_secret': 'aE2x6GYgZFPOJ19Boy6H7gGsr6RWwhhnifKgMtNIqlcGlpz17N',
    'access_token_key': '1223115410486128641-6yyrlupiyZP1WR7nGvSe3eD5jeEXug',
    'access_token_secret': 'Gl6yBicVf7hpKfDuidbTfY906h4fSne9O6OzLOeCamHsd'   
}
