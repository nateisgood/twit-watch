#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:14:45 2020

@author: nate
"""
#%%
import matplotlib.pyplot as plt
from random import randint, choice

xLabsAble = [
    'boobs',
    'jerks',
    'lame-os',
    'intellectual_dark_web',
    'your_moms_tweets',
    'shapiro_hate_views'
]

yLabsAble = [
    'tweets',
    'market_share',
    'influence',
    'media_mentions'
]

#%%
x = range(100)
n = randint(0, 100)
y = []

for i in x:
    y.append(n)
    j = randint(-20, 20)
    n += j
    
    
fig, ax = plt.subplots()

fig.set_size_inches(10, 5)

ax.set_xlabel(choice(xLabsAble))
ax.set_ylabel(choice(yLabsAble))

ax.plot(x, y, choice(['g', 'r', 'b', 'y']))
