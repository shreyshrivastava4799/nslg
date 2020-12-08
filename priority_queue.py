'''
    A simple implementation of Priority Queue using Queue. 
'''
import numpy as np

class PriorityQueue(object): 

    def __init__(self, DEBUG=False, LOG=False): 
        self.DEBUG = DEBUG 

        self.queue = [] 
        self.set = set()
        self.state2queue = {}
  
    # for checking if the queue is empty 
    def is_empty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def push(self, data): 
        
        if tuple(data.state) in self.set:
            # delete the earlier entry and add new one
            for i in range(len(self.queue)):
                if np.array_equal(self.queue[i].state, data.state):
                    del self.queue[i]

            self.queue.append(data) 
            self.state2queue[tuple(data.state)] = data 
        else : 
            self.queue.append(data) 
            self.set.add(tuple(data.state))
            self.state2queue[tuple(data.state)] = data 

        if self.DEBUG:
            print([state.state for state in self.queue])

    # for size of the queue
    def size(self):
        return len(self.queue)
  
    # for popping an element based on Priority 
    def pop(self): 

        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i].cost >= self.queue[max].cost: 
                    max = i 
            
            item = self.queue[max] 
            del self.queue[max] 
            return item 

        except IndexError: 
            print() 
            exit() 

    def check_exists(self, state):
        return tuple(state) in self.set

    def return_state(self, state):
        return self.state2queue[tuple(state)]
            