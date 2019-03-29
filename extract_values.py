#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:13:26 2019

@author: clarissepinel
"""

def extract_values(file):
    values=[]
    f=open(file,'r')
    for line in f:
        line=line.rstrip().split(',')
        values.append(line[1])
    return values



extract_values('ZECUSD.csv')
#print(extract_values('ZECUSD.csv'))
    
    