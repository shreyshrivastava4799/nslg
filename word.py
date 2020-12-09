import numpy as np

DEBUG = False

# once learned embedding are used, embedding size won't be necessary 
embedding_size = 10

class Word:

    def __init__(self, name, cost, pre_cond=None, add_effe=None, del_effe=None):
        self.name = name
        self.cost = cost                # something with how likely a word should be generated
        self.pre_cond = np.random.randint(-1, 2, size=embedding_size)
        self.add_effe = np.random.randint(2, size=embedding_size)
        self.del_effe = np.random.randint(2, size=embedding_size)

    # check if state follows pre-conditions    
    def check_pre_cond(self, state):

        if DEBUG == True:
            self.debug_check_pre_cond(state)
        
        # check if false predicates in pre-condition is false in state
        check_true_pred = np.dot((self.pre_cond==-1).astype(int), (state==0).astype(int)) == np.sum(self.pre_cond==-1)

        if check_true_pred:

            # check if true predicates in pre-condition is true in state
            check_false_pred = np.dot((self.pre_cond==1).astype(int), (state==1).astype(int)) == np.sum(self.pre_cond==1)

            if check_false_pred:
                return True
            else : 
                return False
        else :     
            return False

    # apply the effect of word on the state
    def apply(self, state):

        # delete predicates
        state = state - np.logical_and(self.del_effe>0, state>0).astype(int)

        # return new state after adding predicates
        return np.add(state - np.logical_and(self.add_effe>0, state>0).astype(int), self.add_effe)

    def print_word(self):
        return f'Name: {self.name}\nCost: {self.cost}\nPC: {self.pre_cond}\nAE: {self.add_effe}\nDE: {self.del_effe}\n\n'

    def debug_check_pre_cond(self, state):

        print(self.pre_cond)
        print(state)

        print(self.pre_cond==-1)
        print(state==0)
        print(np.dot(self.pre_cond==-1, state==0))
        print(np.sum(self.pre_cond==-1))

        print(self.pre_cond==1)
        print(state==1)
        print(np.dot(self.pre_cond==1, state==1))
        print(np.sum(self.pre_cond==1))