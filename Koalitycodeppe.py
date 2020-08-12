#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:40:43 2020

@author: Anagha
"""


import pandas as pd
import numpy as np
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
datatot = pd.read_csv("/Users/Anagha/downloads/daily.csv") 
dates= ['20200122', '20200222', '20200322', '20200422', '20200522', '20200622']
#print(dates)
mask = input("Enter mask number: ") 
maskn= int(mask)

states= list()
for i in range(len(datatot)): # this loop creates a list of states
    statestr= str(datatot.loc[i, 'state'])
    if ( statestr in states):
        continue
    else:
        states.append(statestr)

dct = {}
for i in states: # this loop intializes an empty dictionary with each state as a key
    dct['%s' % i] = [i]  


for i in range(len(datatot)): # this loop assigns the number of cases in each state as values in the dictionary
    datestr= str(datatot.loc[i, 'date'])
    if datestr  in dates:
         statestr= str(datatot.loc[i, 'state'])
         for j in dct:
             if statestr in j:
                 
                 posstr= str(datatot.loc[i,'positive'])
                 if posstr== 'nan':
                     dct[j].append('0.0')
                 else:
                     dct[j].append(posstr)

totalavg=0
dctavg = {} 
tempsum= 0
for i in states: # this loop initializes a new empty dictionary with each state as a key
    dctavg['%s' % i] = []       
  
for i in dct:
    tempsum=0
    count=0
    for j in range(len(dct[i])): # this loop assigns the average of COVID cases per month for each state as a value to the state key
        if j == 0 :
            continue
        else: 
            
            val= dct[i][j]
            valint= float(val)
            count+=1
            tempsum= tempsum+valint
            
        
    tempavg= tempsum/6
    
    totalavg= totalavg+tempavg
    
    dctavg[i].append(tempavg) 
        
            
tempavg=0
tempsum=0
percent=0
#print(totalavg)
dctpercent={}
for i in states:
    dctpercent['%s' % i] = []  
for i in dct: # this loop creates a dictionary with states as keys and percent of COVID cases as values 
    tempsum=0
    count=0
    for j in range(len(dct[i])):
        if j == 0 :
            continue
        else: 
            
            val= dct[i][j]
            valint= float(val)
            count+=1
            tempsum= tempsum+valint
            
        
    tempavg= tempsum/6
   
    xpercent= (tempavg/totalavg)*100
    dctpercent[i].append(xpercent) 
    percent= percent+ xpercent
print ('A list of the percentages of COVID cases in each state is given below'+'\n', dctpercent)


dctmasks= dctpercent.copy()
masks= 0
for i in dctmasks: # This loop creates a dictionary with states as keys and the number of masks that should be allocated to each state based on the input of total masks
    for j in range(len(dctmasks[i])):
        dctmasks[i][j]= int((dctmasks[i][j]*maskn)/100)
        masks= dctmasks[i][j]+ masks
        
error= maskn-masks
#print(maskn)
#print(masks)

print(' A list of the number of masks that should be allocated to each state can be seen below based on mask input'+ '\n', dctmasks)
print('error:'+ str(error)+ " masks off")

'''# example of how to do it for one statestates= list()for i in statesstr(i)= set{} #makes state set

#for i in datatot:if('certain date' in str(mydata.loc[i, 'Date'])):add case # for a state  to the state set'''