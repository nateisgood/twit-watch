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
