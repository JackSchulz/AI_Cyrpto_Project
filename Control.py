# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:59:37 2019

@author: lefty
"""

class Control:
    
    def __init__(self, starting_cash, data):
        self.starting_cash = starting_cash
        self.cash = starting_cash
        self.data = data
        self.time_steps = len(data)
        self.inventory = 0 
        
        
    
    def buy(self, percent_buy, market_rate):
        total_asset = self.cash + self.inventory * market_rate
        desired_purchase = total_asset * (percent_buy / 100)
        if desired_purchase > self.cash:
            self.inventory = self.inventory + (self.cash / market_rate)
            
        else:
            self.cash = self.cash - desired_purchase
            self.inventory = self.inventory + (desired_purchase / market_rate)
            
            
    def sell(self, percent_sell, market_rate):
        amount_sold = self.inventory * (percent_sell / 100)
        self.inventory = self.inventory - amount_sold
        new_cash = amount_sold * market_rate
        self.cash = self.cash + new_cash
        
        
    def sell_all(self, market_rate):
        self.sell(100, market_rate)
        
        #bs_alg = BuySell_alg
    def bs_alg(self, risk_rate):
        t = 0
        self.buy(risk_rate, self.data[t])
        t += 1
        #buys or sells all depending until one before the final timestep
        while (t < self.time_steps - 1):
            curr_mr = self.data[t]
            prev_mr = self.data[t-1]
            if curr_mr > prev_mr:
                if self.cash != 0:
                    self.buy(risk_rate, curr_mr)
                
            if curr_mr < prev_mr:
                self.sell(risk_rate, curr_mr)
                
            t += 1
            
        # now at final timesetp
        self.sell_all(self.data[t])
        return self.cash
    
    def all_or_nothing(self):
        risk_rate = 100
        starting_cash = self.starting_cash
        self.cash = starting_cash
        revenue = self.bs_alg(risk_rate)
        profit = revenue - starting_cash
        return profit
    
    
    def cautioned_trader(self):
        risk_rate = 10
        starting_cash = self.starting_cash
        self.cash = starting_cash
        revenue = self.bs_alg(risk_rate)
        profit = revenue - starting_cash
        return profit 
    

        