'''
    A simple implementation of Priority Queue using Queue. 
'''
import numpy as np

class PriorityQueue(object): 

    def __init__(self, DEBUG=False): 
        self.DEBUG = DEBUG 

        self.queue = [] 
        self.set = set()
        self.repr2queue = {}
  
    # for checking if the queue is empty 
    def is_empty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def push(self, data): 
        
        if tuple(data.repr) in self.set:
            # delete the earlier entry and add new one
            for i in range(len(self.queue)):
                if np.array_equal(self.queue[i].repr, data.repr):
                    del self.queue[i]

            self.queue.append(data) 
            self.repr2queue[tuple(data.repr)] = data 
        else : 
            self.queue.append(data) 
            self.set.add(tuple(data.repr))
            self.repr2queue[tuple(data.repr)] = data 

        if self.DEBUG:
            print([state.repr for state in self.queue])

    # for size of the queue
    def size(self):
        return len(self.queue)
  
    # for popping an element based on Priority 
    def pop(self): 

        try: 
            min = 0
            for i in range(len(self.queue)): 
                if self.queue[i].f_cost <= self.queue[min].f_cost: 
                    min = i 
            
            item = self.queue[min] 
            del self.queue[min] 
            return item 

        except IndexError: 
            print() 
            exit() 

    def check_exists(self, state):
        return tuple(state) in self.set

    def return_state(self, state):
        return self.repr2queue[tuple(state)]
            