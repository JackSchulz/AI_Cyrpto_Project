#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:07:41 2019

@author: clarissepinel
"""

# Attempt with Deep Reinforcement Learning


import csv

def extract_data(file):
    f=open(file,'r')
    data=[]
    f.readline()
    for line in f:
        line=line.rstrip().split(',')
        data.append(line)
   
    # 1440 min per day
    # for 180 days 
    # so need to extract from 259,200 lines
    
    #print(data[1])  
    #print(len(data))
    ### now want 1 month of data - 30 days (43200 min)
    selected_data=[]

    # fist line of selected_data is the conversion 
    
    symbol=data[1][2]
    selected_data.append(symbol)

    # range adapted for number of days 
    for i in range(1,43200,2):
        # chosen price is average of open and close

        avg=(float(data[i][3])+float(data[i][6]))/2

        ind=[data[i][1],avg]
        selected_data.append([data[i][1],avg])

    #print(selected_data[129599])
    
    # make new csv file to export for 
    # w+ means not in lib
    file_name=str(symbol)+'.csv'
    new=open(file_name,'w+')
    for line in selected_data[1:]:
        
        l=str(line[0])+','+str(line[1])+'\n'
        new.write(l)
        
    #return selected_data
    
#extract_data('gemini_BTCUSD_2018_1min.csv')
#extract_data('gemini_ETHUSD_2018_1min.csv')
#extract_data('gemini_LTCUSD_2018_1min.csv')
extract_data('gemini_ZECUSD_2018_1min.csv')



def extract_values(file):
    values=[]
    f=open(file,'r')
    for line in f:
        line=line.rstrip().split(',')
        values.append(float(line[1]))
    return values

extracted_values=extract_values('ZECUSD.csv')
#print(extract_values('ZECUSD.csv'))
    
print(extracted_values, len(extracted_values))


import numpy as np
import math

def sigmoid(x):
    return 1/(1+math.exp(-x))


# n-minute state representation, ending at time T 

# data is list of stock prices
# T total final time 
def getStates(data, T, n):
    d=T-n+1
#    if d>=0:
#        block=data[d:T+1]
#    else:
#        block=
        
    block = data[d:T + 1] if d >= 0 else -d * [data[0]] + data[0:T + 1]
    res=[]
    for i in range(n-1):
        res.append(sigmoid(block[i+1]-block[i]))
    print(res)
    return np.array([res])

print(getStates(extracted_values,4,2))
    
    
##########################


# import keras model
# need to install tensorflow

import tensorflow as tf
#import tf.keras
#from tensorflow.python import keras

import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.optimizers import Adam


#for memory 
from collections import deque



# create a deep qlearning agent


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size # normalized previous minutes 
        self.action_size = 3
        # possible actions - buy - sell - sit
        
        # memory is array of experiences explored
        # keep (state, action, reward, next state, done)
        # done = True if final state 
        
        
        # then train neural net with the experiences in memory in smaller batches 
        
        self.memory = deque(maxlen=2000) # change bc different lenghth 
        # memory use deque because of memory 
        
        
        self.inventory=[]
        
        # model name to call specific data set
        self.model_name=model_name
        
        
        self.is_eval=is_eval
        
        
        
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()
        #self.model = load_model("models/" + model_name) if is_eval else self._model()

    def _model(self):
        model = Sequential()
        model.add(Dense(units=64, input_dim=self.state_size, activation="relu"))
        model.add(Dense(units=32, activation="relu"))
        model.add(Dense(units=8, activation="relu"))
        model.add(Dense(self.action_size, activation="linear"))
        
        # learning rate defined here
        model.compile(loss="mse", optimizer=Adam(lr=self.learning_rate))
        return model


# agent decides how to act  
# exploration rate self.epsilon


    import random
    
    def action(self, state):
        if np.random.rand()<=self.epsilon:
            # choose random action
            #takes random of 3 possible actions
            return random.randrange(self.action_size)
        else:
            options=self.model.predict(state)
            
            # check what is returned
            print(options)
            return np.argmax(options[0])


    # use experience in memory to train, using small batches

    def Replay(self,size_of_batch):
        mini_batch=[]
        len_memory=len(self.memory)
        
        for i in range(len_memory-size_of_batch+1,len_memory):
            mini_batch.append(self.memory[i])
        for 
            

