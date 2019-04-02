# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 02:30:53 2019

@author: lefty
"""

import environment as E
import iterator as I
import extract_values as G

def get_profit(cash, data):
    t = len(data)
    ss = E.state_tree(cash, data)
    ss.build_tree(ss.state_start, t)
    ss.build_market_rate(ss.state_start, 0, t)
    q = I.iterator(ss.state_start)
    q.build_next_q(q.q_root, q.mdp_root)
    path, profit = q.find_optimal_path(q.q_root, q.mdp_root)
    return profit

def main():

    cash = 100
    file = 'ETHUSD.csv'
    data = G.Get_Data(file)
    data_list = []
    data_list = data.extract_values()
    t = len(data_list)
    profit = []
    for i in range(t):
        mini_p = get_profit(cash, data_list[i])
        profit.append(mini_p)
        print(i)
        
    avg_profit = sum(profit)/len(profit)
    print("Over the course of 100 different 24 minute intervals, the average profit is:", avg_profit)
    
    
main()