import mesa
from mesa.model import Model

import seaborn as sns
import numpy as np
import pandas as pd 

class MoneyAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        super().__init__(unique_id, model)

        self.wealth = 1
    
    def step(self):
        # The agent's step will go here.
        print(f"Hello, I am agent " + str(self.unique_id) + " and I have " + str(self.wealth) + " wealth.")

class MoneyModel(mesa.Model):

    def __init__(self, N):
        self.num_agents = N

        self.schedule = mesa.time.RandomActivation(self)

        #Create the agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
        
