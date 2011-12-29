'''
Created on Oct 7, 2011

@author: nindza
'''
from time import time
from random import random
from physics.vector2 import Vector2
from physics.Circle import Circle
from physics.Plane import Plane
from physics.DistanceConstraint import DistanceConstraint

import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Fbo

xDistance = Window.width
yDistance = Window.height

def touchingCircle(bodies, touch):
    point = Vector2(touch.x, touch.y)
    
    for circle in bodies[4:]:
        rad = circle.m_radius
        pos = circle.m_position
        dist = point.sub(pos).length()
        if dist <= rad:
            return circle
    return None

    
class BounceBallWidget(Widget):
    
    def __init__(self):
        self.bodies = list()
        self.joints = list()
        self.time = 0
        Clock.schedule_interval(self.main_loop, 1 / 60.)
        self.bodies.append( Plane( Vector2(-1, 0), xDistance ) )
        self.bodies.append( Plane( Vector2(0, -1), yDistance ) )
        self.bodies.append( Plane( Vector2(1, 0), 0 ) )
        self.bodies.append( Plane( Vector2(0, 1), 0 ) )
        
#        for ii in range(0, 4):
#            mass = 20
#            if ii == 0:
#                circle = Circle(mass, Vector2(Window.width / 2.0, Window.height - 20), 0)
#                circle.setColor(color = (random(), random(), random()))
#                self.bodies.append(circle)
#            else:
#                circle = Circle(mass, Vector2.randomRadius(20), mass)
#                circle.setColor(color = (random(), random(), random()))
#                self.bodies.append( circle )
#                
#        for jj in range(4, 7):
#            self.joints.append( DistanceConstraint( self.bodies[jj], self.bodies[jj + 1], 60) )
                
        super(BounceBallWidget, self).__init__()

    def on_touch_down(self, touch):
        touchedCircle = touchingCircle(self.bodies, touch)
        if touchedCircle:
            touch.ud['circle'] = touchedCircle
            touch.ud['mass'] = touchedCircle.m_mass
            touch.ud['time'] = time()
            touchedCircle.m_mass = 0
            touchedCircle.m_velocity = Vector2()
        else:
            mass = int(random() * 10) + 10
            circle = Circle( mass, Vector2(touch.x, touch.y), mass, Vector2(0,-550) )
            color = (random(), random(), random())
            circle.setColor( color )
            self.bodies.append(circle)

    def on_touch_move(self, touch):
        if 'circle' in touch.ud:
            movingCircle = touch.ud['circle']
            movingCircle.m_position = Vector2(touch.x, touch.y)
            if 'start' not in touch.ud:
                touch.ud['start'] = Vector2(touch.x, touch.y)

    def on_touch_up(self, touch):
        if 'circle' in touch.ud:
            touchedCircle = touch.ud['circle']
            touchedCircle.m_mass = touch.ud['mass']
            velocity =  Vector2(touch.x, touch.y).sub(touch.ud['start'])
            touchedCircle.m_velocity = velocity.mulScalar(5)
            print "Throw velocity:", touchedCircle.m_velocity
    
    def clearCanvas(self):
        self.canvas.clear()
    
    def clearBalls(self):
        del self.bodies[4:]
    
    def main_loop(self, dt):
        dt = min(1.0/60.0, dt)
        
        self.gravity(dt)
        self.collide(dt)
        self.solveConstraints(dt)
        self.updatePos(dt)
        self.drawSelf()
        
        # advance time
        self.time += dt
    
    def gravity(self, dt):
        for body in self.bodies:
            body.applyGravity(dt)

    def collide(self, dt):
        numBodies = len(self.bodies)
        for i in xrange(numBodies - 1):
            rbi = self.bodies[i]
            for j in xrange(i + 1, numBodies):
                rbj = self.bodies[j]
                if (rbi.invMass() > 0 or rbj.invMass() > 0):
                    contact = rbi.generateContact(rbj)
#                    print "Contact of", rbi, "and", rbj
                    relV = rbj.m_velocity.sub(rbi.m_velocity)
#                    print "Relative velocity", relV
                    relNV = relV.dot(contact.m_normal)
#                    print "Normalized relative velocity", relNV
                    distance = max(contact.m_distance, -5)
                    remove = relNV + distance / dt
#                    if remove < 0 and contact.m_distance < 0:
                    if remove < 0:
                        # multiply the velocity of the particle by the normal of the hit plane
                        # to get the polar opposite of the velocity. Subtract the twice the result from
                        # the body's velocity to reverse its direction. Split the 2 into elasticity and
                        # 1(to keep the full velocity) to get the elastic effect
#                        rbj.m_velocity = rbj.m_velocity.sub(contact.m_normal.mulScalar(relNV * (1 + rbj.m_elasticity)))
#                        impulse = contact.m_normal.mulScalar(relNV * (1 + rbj.m_elasticity)).divScalar(rbi.invMass() + rbj.invMass())
#                        rbi.m_velocity = rbi.m_velocity.add(impulse.mulScalar(rbi.invMass()))
#                        rbj.m_velocity = rbj.m_velocity.sub(impulse.mulScalar(rbj.invMass()))

                        impulse = remove / (rbi.invMass() + rbj.invMass())
                        rbi.m_velocity = rbi.m_velocity.add( contact.m_normal.mulScalar((1 + rbi.m_elasticity) * impulse * rbi.invMass()))
                        rbj.m_velocity = rbj.m_velocity.sub( contact.m_normal.mulScalar((1 + rbj.m_elasticity) * impulse * rbj.invMass()))

    def solveConstraints(self, dt):
        for joint in self.joints:
            joint.solve(dt)
            
    def updatePos(self, dt):
        for circle in self.bodies:
            circle.integrate(dt)
    
    def drawSelf(self):
        self.clearCanvas()
        with self.canvas:
            for circle in self.bodies:
                if isinstance(circle, Circle):
                    Color(*circle.m_color)
                    circle.drawSelf()


##############################################################
class Bouncer(App):
    
    def __init__(self):
        self.title = "Particle Bouncer"
        self.painter = BounceBallWidget()
        super(Bouncer, self).__init__()
        
    def clearScreen(self, obj):
        self.painter.clearCanvas()
        self.painter.clearBalls()

    def build(self):
        parent = Widget()
        clearbtn = Button(text='Clear')
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        
        clearbtn.bind(on_release=self.clearScreen)
        return parent

    def getPainter(self):
        return self.painter

##############################################################

if __name__ in ('__main__', '__android__'):
    app = Bouncer()
    app.run()
    