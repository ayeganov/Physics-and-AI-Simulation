'''
Created on Nov 1, 2011

@author: nindza
'''

class Contact(object):
    
    def __init__(self, normal, distance, impulse = 0):
        self.m_normal = normal
        self.m_distance = distance
        self.m_impulse = impulse
        
    def __str__(self):
        return "Contact: dist:", str(self.m_distance), "normal:", self.m_normal