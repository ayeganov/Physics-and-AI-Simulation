'''
Created on Oct 24, 2011

@author: nindza
'''

class RigidBody(object):
    '''
    Represents any body in the system.
    '''
    
    def __init__(self, pos, velocity, mass, elasticity = .85):
        '''
        Constructor
        '''
        self.m_position = pos
        self.m_velocity = velocity
        self.m_mass = mass
        self.m_elasticity = elasticity
        
    def integrate(self, dt ):
        self.m_position = self.m_position.add( self.m_velocity.mulScalar( dt ) )

    def applyGravity(self, dt):
        raise Exception("applyGravity must be implemented in sub-classes.")

    def generateContact(self, rb):
        raise Exception("generateContact must be implemented in sub-classes.")
    
    def invMass(self):
        return 1.0/self.m_mass if self.m_mass > 0 else 0

