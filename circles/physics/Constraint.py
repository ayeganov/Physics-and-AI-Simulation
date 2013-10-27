'''
Created on Nov 30, 2011

@author: nindza
'''

class Constraint(object):
    '''
    Constraint object. The building block for physics behavior.
    '''

    def __init__(self, A, B):
        self.bodyA = A
        self.bodyB = B
        assert(self.bodyA.invMass() > 0 or self.bodyB.invMass() > 0, "Constraint's between two infinite mass bodies not allowed.")
        
    def applyImpulse(self, I):
        self.bodyA.m_velocity = self.bodyA.m_velocity.add(I.mulScalar(self.bodyA.invMass()))
        self.bodyB.m_velocity = self.bodyB.m_velocity.sub(I.mulScalar(self.bodyB.invMass()))
        
    def solve(self, dt):
        raise Exception("Derived classes must implement the solve method.")