"""
author: nate
"""
import pandas as pd
import json
import os

fns = [fn for fn in os.listdir('some_data/av_club/')]
fns.sort()

for fn in fns:
    print(fn)
