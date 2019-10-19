'''
Created on 25/03/2013

@author: paco
'''
import math
from pyHotDraw.Geom.pyHPoint import pyHPoint
from pyHotDraw.Figures.pyHAttributes import pyHAttributeColor




class pyHAbstractFigure(object):
    def __init__(self):
        self.attributes={}
        self.changedFigureObservers=[]
        c=pyHAttributeColor(0,0,0)
        self.setColor(c)
        #this line gives maximun recursiondeep import error
        #self.toolBoxConnectors=pyHLocatorConnector.ToolBoxRectangleConnectors(self)
    def getAttribute(self, k):
        return self.attributes[k]
    def setAttribute(self,k,v):
        self.attributes[k]=v
    def setColor(self,c):
        self.setAttribute("COLOR",c)
    def getDisplayBox(self):
        pass
    def setDisplayBox(self,r):
        pass
    def containPoint(self,p):
        db = self.getDisplayBox()
        x_condition = db.getX() <= p.getX() <= db.getX() + db.getWidth()
        y_condition = db.getY() <= p.getY() <= db.getY() + db.getHeight()
        return x_condition and y_condition


    def move(self,x,y):
        pass
    def draw(self,g):
        for v in self.attributes.values():
            v.draw(g)
            
#Abstract handles methods
    def getHandles(self):
        handles=[]
        r=self.getDisplayBox()
        x=r.getX()
        y=r.getY()
        w=r.getWidth()
        h=r.getHeight()
        handles.append(pyHNullHandle(self,pyHPoint(x,y)))
        handles.append(pyHNullHandle(self,pyHPoint(x+w,y)))
        handles.append(pyHNullHandle(self,pyHPoint(x,y+h)))
        handles.append(pyHNullHandle(self,pyHPoint(x+w,y+h)))
        return handles
#Connector methods
    def getConnectors(self):
        return pyHLocatorConnector.ToolBoxRectangleConnectors(self)
    def findConnector(self,p):
        minD=1e90
        for c in self.getConnectors():
            r=c.getDisplayBox()
            pc=pyHPoint(r.getX()+r.getWidth()/2,r.getY()+r.getHeight()/2) #central point of connector
            dx=pc.getX()-p.getX()
            dy=pc.getY()-p.getY()
            d=math.sqrt(dx*dx+dy*dy)
            if d<minD:
                minD=d
                closestConnector=c
        return closestConnector

    #Observer pattern methods
    def addChangedFigureObserver(self,fo):  
        self.changedFigureObservers.append(fo)
    def notifyFigureChanged(self):
        for fo in self.changedFigureObservers:
            fo.figureChanged(self)        




from pyHotDraw.Locators.pyHRelativeLocator import pyHRelativeLocator
from pyHotDraw.Connectors.pyHLocatorConnector import pyHLocatorConnector
from pyHotDraw.Handles.pyHNullHandle import pyHNullHandle