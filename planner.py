'''
This file contains the implementation of a planner which generates a sequence of actions signifying 
words.
'''

import numpy as np
from priority_queue import PriorityQueue
import copy
from datetime import datetime

LOG = True
DEBUG = False
embedding_size = 2

class State:

    def __init__(self, cost, state, path):
        self.cost = cost 
        self.path = path
        self.state = state 
    
    def print_state(self):
        return f'Cost: {self.cost}\nPath: {self.path}\nState: {self.state}\n\n'

class Word:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.pre_cond = np.random.randint(2, size=embedding_size)
        self.add_effe = np.random.randint(2, size=embedding_size)
        self.del_effe = np.random.randint(2, size=embedding_size)

    # check if state follows pre-conditions    
    def check_pre_cond(self, state):

        cond_sati = np.logical_and(self.pre_cond>0, state>0).astype(int)
        if np.sum(cond_sati) != np.sum(self.pre_cond):
            return False
        else : 
            return True 

    # apply the effect of word on the state
    def apply(self, state):

        state = state - np.logical_and(self.del_effe>0, state>0).astype(int)
        return np.add(state - np.logical_and(self.add_effe>0, state>0).astype(int), self.add_effe)

    def print_word(self):
        return f'Name: {self.name}\nCost: {self.cost}\nPC: {self.pre_cond}\nAE: {self.add_effe}\nDE: {self.del_effe}\n\n'

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
            return self.actions  

        s_state = State(0, start, [])
    
        if self.LOG:
            self.file.write(f'Start state: {start}\nEnd state: {end}\n')

        OPEN = PriorityQueue(DEBUG, LOG)

        # insert the start state in OPEN list
        OPEN.push(s_state)

        while not OPEN.is_empty():

            c_state = OPEN.pop()
                            
            if self.LOG:
                self.file.write(c_state.print_state())

            # check if end state reached
            if tuple(c_state.state) == tuple(end):
                print(f'End state reached\n')
                return c_state.path 

            # select a set of actions based on the current state
            actions = select_actions(c_state)

            # apply actions to find the next states
            for action in actions:

                if not action.check_pre_cond(c_state.state):
                    continue 
                
                n_path = copy.deepcopy(c_state).path
                n_path.append(action.name)
                n_state = State(action.cost, action.apply(c_state.state),n_path)
                
                # check if this state already present in OPEN list
                if OPEN.check_exists(n_state.state):
                    
                    # insert only if the cost of earlier state is more than next state
                    e_state = OPEN.return_state(n_state.state)
                    if e_state.cost > n_state.cost:
                        OPEN.push(n_state)

                else : 
                    OPEN.push(n_state)    

        return []

        
# Example 
if __name__ == "__main__":

    vocab = ['hello', 'my', 'name', 'is', 'Shrey', '.']
    actions = []
    for word in vocab:
        actions.append(Word(word, np.random.randint(10)))

    start =  np.random.randint(2, size=embedding_size)
    end =  np.random.randint(2, size=embedding_size)

    planner = Planner(actions, LOG)
    print(planner.plan(start, end))



