#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:08:53 2019

@author: clarissepinel
"""


'''

extract data -
take data from 2018, july to december 
every 2 min
price is average of open and close

'''
#
#class Get_Data:
#    
#    
#    def extract_data(file):
#        f=open(file,'r')
#        data=[]
#        f.readline()
#        for line in f:
#            line=line.rstrip().split(',')
#            data.append(line)
#       
#        # 1440 min per day
#        # for 180 days 
#        # so need to extract from 259,200 lines
#        
#        #print(data[1])  
#        #print(len(data))
#        
#        selected_data=[]
#    
#        # fist line of selected_data is the conversion 
#        
#        #symbol=data[1][2]
#        #selected_data.append(symbol)
#    
#    
#        for i in range(1,400000,2):
#            # chosen price is average of open and close
#    
#            avg=(float(data[i][3])+float(data[i][6]))/2
#    
#            ind=[data[i][1],avg]
#            selected_data.append([data[i][1],avg])
#            
#            
#        blocks_of_21=[]
#        
#        count=1
#        for j in range(100):
#            block_of_21=[]
#            for i in range(21):
#                block_of_21.append(selected_data[count])
#                count+=1
#            blocks_of_21.append(block_of_21)
#        print(len(blocks_of_21),len(block_of_21))
#            
#            
#    
#        #print(selected_data[129599])
##        
##        
##        # make new csv file to export for 
##        # w+ means not in lib
##        file_name=str(symbol)+'.csv'
##        new=open(file_name,'w+')
##        for line in selected_data[1:]:
##            
##            l=str(line[0])+','+str(line[1])+'\n'
##            new.write(l)
##            
##            
##            
##        def extract_values(file):
##    values=[]
##    f=open(file,'r')
##    for line in f:
##        line=line.rstrip().split(',')
##        values.append(float(line[1]))
##    return values
##
##
##
##extract_values('ZECUSD.csv')
###print(extract_values('ZECUSD.csv'))
##    
#    
#
#        
#        
#        
#        
#        
#        #return selected_data
#        
#Get_Data.extract_data('gemini_BTCUSD_2018_1min.csv')
#    #extract_data('gemini_ETHUSD_2018_1min.csv')
#    #extract_data('gemini_LTCUSD_2018_1min.csv')
#    #extract_data('gemini_ZECUSD_2018_1min.csv')
#    
        
        
        
        

    
