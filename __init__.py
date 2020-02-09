"""
author: nate
"""
#%%
import pandas as pd
import json
import os
import re

fn = 'some_data/av_club.json'

with open(fn, 'r') as file:
    views = json.load(file)
    