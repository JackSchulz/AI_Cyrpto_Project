# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:58:54 2019

@author: lefty
"""

import environment as E

class iterator:
    
    def __init__(self, mdp_root):
        self.mdp_root = mdp_root
        self.q_root = E.Node(self.reward(mdp_root))
        self.discount = .9
        
    
    def reward(self, state):
        s = state.data
        reward = s[0] + s[1] * s[2]
        return reward
    
    
    def transition(self, action):
        if action == "hold":
            return 1
        #90% chance a trade sucessfully goes through
        else:
            return .9
        
    def next_state(self, mdp_node, action):
        if action == "hold":
            return mdp_node.left
        # action == "trade"
        else:
            return mdp_node.right
        

    def build_next_q(self, q_node, mdp_node):
        if mdp_node.left == None:
            return
        q_node.left = E.Node(self.transition("hold")*self.reward(mdp_node.left))
        q_node.right= E.Node(self.transition("trade")*self.reward(mdp_node.right))
        self.build_next_q(q_node.left, mdp_node.left)
        self.build_next_q(q_node.right, mdp_node.right)
     
    def find_optimal_path(self, q_node, mdp_node):
        v = q_node
        mdp = mdp_node
        path = []
        while v.left != None:
            hold = v.left.data
            trade = v.right.data
            if hold > trade:
                path.append("hold")
                v = v.left
            
            elif trade > hold:
                path.append("trade")
                v = v.right
            
            else:
                diverted_path_hold, h_profit = self.find_optimal_path(v.left)
                diverted_path_trade, t_profit = self.find_optimal_path(v.right)
                if h_profit >= t_profit:
                    path.append("hold")
                    v = v.left
                else:
                    path.append("trade")
                    v = v.right
                    
        for direction in path:
            if direction == "hold":
                mdp = mdp.left
            else:
                mdp = mdp.right
        max_profit = self.reward(mdp)    
        return path, max_profit
                
                
 # test
"""      
def main():
    data = [1000,2000,3000,4000,50000,10000,7000,8000,9000,10000,11000,9000,13000,14000,15000,16000,10000,18000,19000,20000,5000]
    t = len(data)
    print(t)
    cash = 100
    ss = E.state_tree(cash, data)
    ss.build_tree(ss.state_start, t)
    ss.build_market_rate(ss.state_start, 0, t)
    q = iterator(ss.state_start)
    q.build_next_q(q.q_root, q.mdp_root)
    path, profit = q.find_optimal_path(q.q_root, q.mdp_root)
    print(path)
    print(profit)
    #q.build_q_tree(q.q_root, ss.state_start, 3)
main()
"""
            