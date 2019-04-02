# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:50:10 2019

@author: lefty
"""

class state_tree:
    
    def __init__(self, start_cash, market_data):

        self.market_data = market_data
        self.t = len(self.market_data)
        # state = [cash, inventory, market_price]
        self.state_start = Node([start_cash, 0, 0])

        
    
    def next_state(self, curr_state, action):
        state = curr_state.data
        if action == "hold":
            next_state = state[:]
            next_state[2] = state[2] + 1
        
        if action == "trade":
            # if there is no cash, sell inventory
            if state[0] == 0:
                next_state = [state[1] * self.market_data[state[2]], 0, state[2] + 1]

            # if there is cash, spend all of it to buy inventory
            else:
                next_state = [0, state[0] / self.market_data[state[2]], state[2] + 1]
                
                
            
        new_node = Node(next_state)
        return new_node
            
        
    def build_children(self, node_state, remaining_levels):
        if remaining_levels == 1:
            return None
        #print(remaining_levels)
        node_state.left = self.next_state(node_state, "hold")
        node_state.right = self.next_state(node_state, "trade")
        self.build_children(node_state.left, remaining_levels-1)
        self.build_children(node_state.right, remaining_levels-1)
        
    def build_tree(self, root, depth):
        self.build_children(root, depth)
        
    def build_market_rate(self, root, market_index, depth):
        if depth == 0:
            return
        root.data[2] = self.market_data[market_index]
        market_index += 1
        self.build_market_rate(root.left, market_index, depth-1)
        self.build_market_rate(root.right, market_index, depth-1)
      
    
        
        
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
#testing
"""
def main():
    data = [5,2,1]
    cash = 10
    ss = state_tree(cash, data)
    ss.build_tree(ss.state_start, 3)
    ss.build_market_rate(ss.state_start, 0, 3)
    print(ss.state_start.data)
    print(ss.state_start.left.data)
    print(ss.state_start.right.data)
    print(ss.state_start.left.left.data)
    print(ss.state_start.left.right.data)
    print(ss.state_start.right.left.data)
    print(ss.state_start.right.right.data)
    
main()
"""
