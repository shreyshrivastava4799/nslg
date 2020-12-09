'''
This file contains the implementation of a planner which generates a sequence of actions signifying 
words.
'''

import copy
import numpy as np
from datetime import datetime

from word import Word
from state import State
from priority_queue import PriorityQueue

LOG = True
DEBUG = False
embedding_size = 10

class Planner:

    def __init__(self, actions, LOG):
        self.actions = actions
        self.LOG = LOG

        if self.LOG:
            self.file = open("log-"+datetime.now().strftime("%m-%d-%Y-%H-%M-%S")+".txt", "w") 
            for action in actions:
                self.file.write(action.print_word())


    def plan(self, start, end):

        def select_actions(state):
            '''
                1. Clustering based on pre-conditions as a lot of words would have intersecting pre-conditions
                2. Sort on the basis of f_cost
            '''
            return self.actions  

        s_state = State(0, start, [])
    
        if self.LOG:
            self.file.write(f'Start state: {start}\nEnd state: {end}\n\n')

        OPEN = PriorityQueue(DEBUG)

        # insert the start state in OPEN list
        OPEN.push(s_state)

        while not OPEN.is_empty():

            c_state = OPEN.pop()
                            
            if self.LOG:
                self.file.write(c_state.print_state())

            # check if end state reached
            if tuple(c_state.repr) == tuple(end):
                print(f'End state reached\n')
                return c_state.path 

            # select a set of actions based on the current state
            actions = select_actions(c_state)

            # apply actions to find the next states
            for action in actions:

                if not action.check_pre_cond(c_state.repr):
                    continue 
                
                n_path = copy.deepcopy(c_state).path
                n_path.append(action.name)
                n_state = State(action.cost, action.apply(c_state.repr),n_path)
                n_state.update_h_and_f_cost(end)            

                # check if this state already present in OPEN list
                if OPEN.check_exists(n_state.repr):
                    
                    # insert only if the cost of earlier state is more than next state
                    e_state = OPEN.return_state(n_state.repr)
                    if e_state.f_cost > n_state.f_cost:
                        OPEN.push(n_state)

                else : 
                    OPEN.push(n_state)    

        return []

        
# Example 
if __name__ == "__main__":

    vocab = ['hello', 'my', 'name', 'is', 'Shrey', '.', 'I', 'am', 'trying', 'to', 'create', 'a', 'neuro', 'symbolic', 'language', 'generation', 'system']
    actions = []
    for word in vocab:
        actions.append(Word(word, np.random.randint(10)))

    start =  np.random.randint(2, size=embedding_size)
    end =  np.random.randint(2, size=embedding_size)

    planner = Planner(actions, LOG)
    print(planner.plan(start, end))



