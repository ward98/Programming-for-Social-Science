# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:07:07 2020

@author: Cameron
"""

#Import always at the top  
import random 

#Agent Class captures behaviours of agents
class Agent():
    #Creating the construtor methods
    def __init__(self, environment, agents, y, x):
        self.y = random.randint(0,len(environment) - 1)
        self.x = random.randint(0,len(environment[0]) - 1)
        self.environment = environment
        self.store = 0 
        self.agents = agents
        self.y = y
        self.x = x
        
#Define the share with neighbours function 
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))

#Define the move function
    def move(self):
        maxy = len(self.environment)
        if random.random() < 0.5:
            self.y = (self.y + 1) % maxy
        else:
            self.y = (self.y - 1) % maxy
        maxx = len(self.environment[0])
        if random.random() < 0.5:
            self.x = (self.x + 1) % maxx
        else:
            self.x = (self.x - 1) % maxx
            
#Define the eat function 
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10   
            
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5