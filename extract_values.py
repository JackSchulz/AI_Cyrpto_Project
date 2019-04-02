#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:13:26 2019

@author: clarissepinel
"""

'''
def extract_values(file):
    values=[]
    f=open(file,'r')
    for line in f:
        line=line.rstrip().split(',')
        values.append(float(line[1]))
    print(len(values),values[21360:21370])
    return values



extract_values('ETHUSD.csv')
#print(extract_values('ZECUSD.csv'))
'''  
    
"""
Created on Fri Mar 29 12:13:26 2019
@author: clarissepinel
"""

import random

class Get_Data:
    def __init__(self, file):
        self.file = file
    
    def extract_values(self, file):
        values=[]
        f=open(file,'r')
        for line in f:
            line=line.rstrip().split(',')
            #print(line)
            values.append(float(line[1]))
            #print(line[1])
        #print(values)
        #print(len(values))
        values=values[1:]
        return values
        
        
#    file = 'ETHUSD.csv'
#    data = G.Get_Data(file)
#    data_list = []
#    data_list = data.extract_values()
#    t = len(data_list)
        
        
        
        
    def blocks(self, values):
        blocks_of_21=[]
        #values.extract_values()
        for i in range(0,len(values)-20//21):
            block=[]
            
            for j in range()
                block.append(values[i+j])
                
                
                
                
            
        
        
        
        
        count=1
        for j in range(40):
            block_of_21=[]
#            for i in range(21):
#                block_of_21.append(values[i])
#                count+=1
#            blocks_of_21.append(block_of_21)
#        print(len(values))
#        print(len(blocks_of_21),len(block_of_21))
#        print(blocks_of_21[0])
#        print(blocks_of_21[1])
#        

        
        return blocks_of_21
    
    
    
    def random_block(self, blocks_of_21):
        random_blocks=[]
        
        
        
        
        
        
        
        
        #seen_index=[]
        
        for i in range(0,21):
            seen_index=[]
            r=range(random.randint(1,40))
            block_of_21=[]
            for j in r:
                block_of_21.append(blocks_of_21[j])
            
        
        #for i in range(0,10):
            
        
            
            #r=random.randint(100)
            if blocks_of_21[r] not in random_blocks:
                random_blocks.append(blocks_of_21[r])
        print(len(random_blocks),len(random_blocks))
        print(random_blocks[0])
        print(random_blocks[1])
    
        return random_blocks
        
        #for i in random.randint(0,21):
            
            
    
#def main():
    
    
#main()
    
    
#file='ETHUSD.csv'
file='ETHUSD.csv'
data=Get_Data(file)
pairs=data.extract_values(file)
data_list=[]
data_list=data.blocks(file)


#random_list=data.random_block(data_list)


#Get_Data.extract_values(file)
#print(extract_values('ZECUSD.csv'))
    
    
