#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 25/03/2013

@author: paco
'''
from pyHotDraw.Geom.pyHRectangle import pyHRectangle
from pyHotDraw.Figures.pyHAbstractFigure import pyHAbstractFigure

class pyHRectangleFigure(pyHAbstractFigure):
    def __init__(self,x0,y0,w,h):
        pyHAbstractFigure.__init__(self)
        self.x0=x0
        self.y0=y0
        self.w=w
        self.h=h

    def getDisplayBox(self):
        return pyHRectangle(self.x0,self.y0,self.w,self.h)

    def setDisplayBox(self,r):
        self.x0=r.getX()
        self.y0=r.getY()
        self.w =r.getWidth()
        self.h =r.getHeight()
        #send event to observers
        self.notifyFigureChanged()
    def move(self,dx,dy):
        self.x0+=dx
        self.y0+=dy
        #send event to observers
        self.notifyFigureChanged()
    def draw(self,g):
        pyHAbstractFigure.draw(self,g)
        g.drawRect(self.x0,self.y0,self.w,self.h)
    #visitor method
    def visit(self,visitor):
        return visitor.visitRectangleFigure(self)
        

    def set_x(self, x):
        self.x0 = x

    def set_y(self, y):
        self.y0 = y

    def get_x(self):
        return self.x0

    def get_y(self):
        return self.y0

    x = property(get_x, set_x)
    y = property(get_y, set_y)

