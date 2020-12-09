class State:

    def __init__(self, cost, repr, path):
        self.g_cost = cost      # captures syntactic and semantic validity of current path
        self.h_cost = 0         # captures distance from the end state's representation
        self.f_cost = 0 
        self.path = path
        self.repr = repr 
        self.calc_g_cost()
    
    def print_state(self):
        return f'Cost: {self.g_cost} + {self.h_cost} = {self.f_cost}\nPath: {self.path}\nRepresentation: {self.repr}\n\n'

    def calc_g_cost(self):
        self.g_cost = 10         # should depend upon path

    def update_h_and_f_cost(self, end):
        self.h_cost = 10         # should depend on end state's representation and current repr
        self.f_cost = self.g_cost + self.h_cost
