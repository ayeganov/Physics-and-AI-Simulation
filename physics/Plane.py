'''
Created on Nov 1, 2011

@author: nindza
'''

from physics.rigidbody import RigidBody
from physics.vector2 import Vector2
from physics.Circle import Circle
from physics.Contact import Contact

class Plane(RigidBody):
    
    def __init__(self, normal, distance):
        self.m_normal = normal
        self.m_distance = distance
        super(Plane, self).__init__(self.m_normal.mulScalar(-self.m_distance), Vector2(), 0, 1)
    
    def generateContact(self, rb):
        if isinstance(rb, Circle):
#            distance = self.distanceToPlane(rb.m_position)
#            impulse = 0
#            relV = rb.m_velocity.sub(self.m_velocity)
#            if distance <= 0:
#                body.m_velocity.sub(plane.m_normal.mulScalar(relNV * (1 + rb.m_elasticty)))
            return Contact(self.m_normal, self.distanceToPlane(rb.m_position) - rb.m_radius )
        
        raise Exception("Unhandled case. Plane contact with", rb)
    
    def distanceToPlane(self, p):
        return p.dot(self.m_normal) + self.m_distance
    
    def applyGravity(self, dt):
        # gravity doesn't affect planes
        pass
    
    def __str__(self):
        return str(self.m_normal)