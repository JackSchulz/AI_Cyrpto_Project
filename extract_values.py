#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:13:26 2019

@author: clarissepinel
"""
class Get_Data:
    def __init__(self, file):
        self.file = file
    def extract_values(self):
        values=[]
        f=open(self.file,'r')
        for line in f:
            line=line.rstrip().split(',')
            values.append(float(line[1]))
        
        
        blocks_of_21=[]
        
        count=1
        for j in range(100):
            block_of_21=[]
            for i in range(20):
                block_of_21.append(values[count])
                count+=1
            blocks_of_21.append(block_of_21)
        print(len(blocks_of_21),len(block_of_21))
        
        
        return blocks_of_21
    
    
    
#Get_Data.extract_values('ZECUSD.csv')
#print(extract_values('ZECUSD.csv'))
    
    
