#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:31:54 2019

@author: clarissepinel
"""

'''
# not sure about features

features are the f(s,a)


# not sure about how to calculate reward (where)

get leagal actions function - if not terminal state, if enough money? 
 assumed implemented but not 


# neet def getLegalActions

'''

import util

class ApproximateQAgent:
    
    def __init__(self,):
        
        self.discount=discount
        self.learning_rate=learning_rate
        
        # not sure need q_table
        self.q_table=util.Counter()
        self.weights=util.Counter()
    
    def getQValue(self, state, action):
        '''
        return the q fro a state and action
        new q is weghts* feature vector 
        
        incomplete
        
        '''
        #pass
        # don;t know for features #
        #     features = self.featExtractor.getFeatures(state, action)
        #   
        #features= extract feature corresponding to state and action somehow
        
        
        # init q_value
        q_value=0.0
        for feature in features:
            # weight of corresponding feature * the feature in the list of features
            q_value+=self.weights[feature]*features[feature]
         
         # if terminal state, return 0.0   
            
        return q_value
    
    
        
    def getAction(self, state):
        
        ### not done ###
        
        '''
        find action to take in current state
        use random action to epsilon % of time
        take best action rest of time
        
        if at terminal state, choose None
        
        should legal actions include if have enoguh money to execute action?
        
        
        '''
        
        
        
        
        
    def getValue(self, state):
        '''
        out of legal actions
        choose largest q value
        
        
        '''
        for action in self.getLegalActions(state):
            q_values=[self.getQValue(state, action)]
        return max(q_values)
            
  
    
            
    def update(self, satte, action, nextState,reward):
        '''
        update weights 
        use formulas
        difference= reward + discount(max qvalue of s',a') - qvalue(s,a)
        max qvalue = value
        '''
        difference=reward + (self.discount*self.getValue(nextState)) - self.getQValue(state,action)
        
        ### same features unsure
        
        # features = self.featExtractor.getFeatures(state, action)
        for feature in features:
            # update weight 
            self.weights[feature]+= self.learning_rate * difference * features[feature]

        
        
        
        
        
        
        
        
