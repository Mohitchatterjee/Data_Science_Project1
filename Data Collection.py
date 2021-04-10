# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:48:21 2021

@author: im_chatterjee
"""
 
import glassdoor_scraper as gs
import pandas as pd 

path = "C:/Users/hp/Desktop/Data analytics/Data Science Project/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

