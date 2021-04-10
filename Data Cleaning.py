# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:18:02 2021

@author: im_chatterjee
"""

import pandas as pd
df = pd.read_csv('DataScientist.csv')

# For Salary Parsing

df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0 )  # make one column for where salary estimate has 'Per Hour' test too. 

# df == df[df['Salary Estimate'] != '-1']  if your Salary Estimate feature has -1 

Salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])  # this is for remove (Glassdoor est.) from Salar Estimate Feature

remove_kD = Salary.apply(lambda x: x.replace('K','').replace('$',''))  # remove $ and K sign from Salary Estimate  D = $

remove_hour = remove_kD.apply(lambda x: x.lower().replace('per hour',''))  # remove 'per hour' text

df['min_salary'] = remove_hour.apply(lambda x: int((x.split('-')[0])))
df['max_salary'] = remove_hour.apply(lambda x: int((x.split('-')[1])))
df['avg_salary'] = (df['min_salary'] + df['max_salary'])/2


# Comapany bname Text only

df['Company_Text'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis = 1)


# State Field

df['Job_State'] = df['Location'].apply(lambda x: x.split(',')[1])
df.Job_State.value_counts()


# Same JOb_Location as HeadQuarter

df['Same_location'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# Age of Company

df['Age_Company'] = df.Founded.apply(lambda x: x if x < 0 else 2021 - x)

# Job_Description Parsing (eg. python, R, Excel, spark, AWS etc...)

df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R Studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)


df.columns
df = df.drop(['Unnamed: 0'],axis = 1)
df.head()
df.to_csv('Data_Science_Salary_Clean.csv', index = False)


df = pd.read_csv('Data_Science_Salary_Clean.csv')








