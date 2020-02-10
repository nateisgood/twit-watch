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

api = twitter.Api(consumer_key=creds['consumer_key'],
                  consumer_secret=creds['consumer_secret'],
                  access_token_key=creds['access_token_key'],
                  access_token_secret=creds['access_token_secret'])
# I get this error when i try this: TypeError: 'module' object is not callable

results = api.GetSearch('Bojack Horseman')
