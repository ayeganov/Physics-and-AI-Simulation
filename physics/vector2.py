'''
Created on Oct 24, 2011

@author: nindza
'''

import math
from random import random
import Point

class Vector2(object):
    
    def __init__(self, x = 0, y = 0):
        self.m_x = x
        self.m_y = y

    def add(self, vector2): 
        return Vector2(self.m_x + vector2.m_x, self.m_y + vector2.m_y)
    
    def addX(self, vec2): 
        return Vector2(self.m_x + vec2.m_x, self.m_y)
  
    def addY(self, vec2): 
        return Vector2(self.m_x, self.m_y + vec2.m_y)
  
    def sub(self, vec2): 
        return Vector2(self.m_x - vec2.m_x, self.m_y - vec2.m_y)

    def mul(self, vec2): 
        return Vector2(self.m_x * vec2.m_x, self.m_y * vec2.m_y)

    def mulScalar(self, scalar): 
        return Vector2(self.m_x * scalar, self.m_y * scalar)
    
    def divScalar(self, scalar):
        return Vector2(self.m_x / scalar, self.m_y / scalar)
      
    def dot(self, vec2): 
        return self.m_x * vec2.m_x + self.m_y * vec2.m_y
      
    def lenSqr(self): 
        return self.dot(self)

    def length(self): 
        return math.sqrt(self.lenSqr())
      
    def unit(self):
        ''' Unit vector form. '''
        invLen  = 1.0 / self.length()
        return self.mulScalar(invLen)

    def floor(self):
        return Vector2(math.floor(self.m_x), math.floor(self.m_y))
    
    def clamp(self, minVec2, maxVec2 ):
        return Vector2( max( min(self.m_x, maxVec2.m_x), minVec2.m_x), max(min(self.m_y, maxVec2.m_y), minVec2.m_y) )
    
    def perp(self):
        return Vector2(-self.m_y, self.m_x)
    
    def negate(self):
        return Vector2(-self.m_x, -self.m_y)

    def equal(self, vec2):
        return self.m_x == vec2.m_x and self.m_y == vec2.m_y

    @staticmethod
    def fromAngle(angle): 
        return Vector2(math.cos(angle), math.sin(angle))
    
    @staticmethod
    def randomRadius(radius):
        return Vector2(random() * 2 - 1, random() * 2 - 1).mulScalar(radius)
    
    @staticmethod
    def fromPoint(point):
        return Vector2(point.x,point.y)

    def point(self):
        return Point(self.m_x, self.m_y)
  
    def clear(self):
        self.m_x=0
        self.m_y=0

    def clone(self):
        return Vector2(self.m_x, self.m_y)

    def __str__( self ):
        return "x = " + str(self.m_x) +", y = " + str(self.m_y)
    