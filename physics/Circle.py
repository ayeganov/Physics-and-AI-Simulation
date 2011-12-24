'''
Created on Nov 1, 2011

@author: nindza
'''

from kivy.graphics import Ellipse
from kivy.core.window import Window
from physics.rigidbody import RigidBody
from physics.vector2 import Vector2
from physics.Contact import Contact
from Globals import Globals

class Circle(RigidBody):

    def __init__(self, radius, pos, invMass, velocity = Vector2()):
        self.m_radius = radius
        super(Circle, self).__init__(pos, velocity, invMass)

    def drawSelf(self):
#        globalPos = converter(self.m_position)
#        globalRad = converter(self.m_radius)
        Ellipse(pos=(self.m_position.m_x - self.m_radius, self.m_position.m_y - self.m_radius), size=(self.m_radius * 2, self.m_radius * 2))

    def setColor(self, color = None):
        self.m_color = color
        
    def applyGravity(self, dt):
        if self.invMass() > 0:
            self.m_velocity = self.m_velocity.add( Globals.gravity.mulScalar(dt) )

    def generateContact(self, rb):
        if isinstance(rb, Circle):
            minDist = self.m_radius + rb.m_radius
            vecDist = rb.m_position.sub(self.m_position)
            dist = vecDist.length()
            penetration = dist - minDist
            
            # wth is this?
            if dist == 0.0:
                print "WTF"
                return Contact(Vector2(1,0), -minDist)
            
            impulse = 0
#            relV = self.m_velocity.sub(rb.m_velocity)
#            normal = vecDist.unit()
#            invMassSum = self.m_invMass + rb.m_invMass
#            
#            if penetration <= 0.0:
#                #collision has occurred, calculate the impulse
##                I = (1+e)*N*(Vr . N) / (1/Ma + 1/Mb)
#                impulse = normal.mulScalar(1 + self.m_elasticity).mulScalar(relV.dot(normal)).mulScalar(1.0 / invMassSum)
            return Contact(vecDist.unit(), penetration, impulse)

        raise Exception("Unhandled case. Circle contact with", rb)
    
    def __str__(self):
        return str(self.m_position.m_x) + ", " + str(self.m_position.m_y) + " = " + str(self.m_radius)