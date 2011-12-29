'''
Created on Nov 30, 2011

@author: nindza
'''

from physics.Constraint import Constraint

class DistanceConstraint(Constraint):
    '''
    Concrete implementation of a distance constraint.
    '''


    def __init__(self, A, B, distance):
        self.m_distance = distance
        super(DistanceConstraint, self).__init__(A, B)
        
        
    def solve(self, dt):
        axis = self.bodyB.m_position.sub(self.bodyA.m_position)
        curDist = axis.length()
        unitAxis = axis.unit()
        
        # calculate relative velocity in the axis, we want to remove this
        relV = self.bodyB.m_velocity.sub(self.bodyA.m_velocity).dot(unitAxis)
        
        relDist = curDist - self.m_distance
        
        # calculate impulse to solve
        remove = relV + relDist / dt
        impulse = remove / (self.bodyA.invMass() + self.bodyB.invMass())
        
        I = unitAxis.mulScalar(impulse)
        
        self.applyImpulse(I)
        
        