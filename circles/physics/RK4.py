'''
Created on Dec 18, 2011

@author: nindza
'''

class State(object):
    '''
    classdocs
    '''


    def __init__(self, pos = 0, vel = 0, mass = 0):
        self.position = pos
        self.velocity = vel
        self.mass = mass
        
        
class Derivative(object):
    
    def __init__(self, dPos = 0, dVel = 0):
        self.dPos = dPos
        self.dVel = dVel
        
        
def evaluate(initState, time, delta, derivative):
    state = State(initState.position + derivative.dPos * delta, initState.velocity + derivative.dVel * delta)
    
    output = Derivative()
    output.dPos = state.velocity
    output.dVel = force(initState, time + delta)
    return output

def force():
        