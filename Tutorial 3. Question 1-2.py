# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:38:11 2017

@author: 214576460
"""

import numpy as np

#question 1: creating a class with x, y, G as gravitational constant and number of particles
class particle:
    def __init__(self,n=100, G=1.0, m=1, dt=0.01):
        #creating dictionary
        self.dict={}
        self.dict['n']=n #key n in self.dict has value n=1000
        self.dict['G']=G #key G in self.dict has value G=1.0
        self.dict['dt']=dt
        #positions
        self.x=np.random.randn(n)
        self.y=np.random.randn(n)
        #masses
        self.m=np.ones(self.dict['n']) * (m / self.dict['n'])
        #velocities: intially set to zero
        self.vx=np.zeros(n)
        self.vy=np.zeros(n)
        
       
        #print self.dict
        
        #calculating potential energy of particles
    def potential(self):
        potent=np.zeros(self.dict['n'])
        
        for i in range(0, self.dict['n']):#method to calculate potential and force
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            rsquared=dx*dx+dy*dy
            r=np.sqrt(rsquared)
            #rinv=1.0/r
            #rinv[i]=0
            potent[i]=np.sum(self.dict['G']*self.m[i]*self.m)
        return potent
    def force(self):  
        self.Fx=np.zeros(self.dict['n'])
        self.Fy=np.zeros(self.dict['n'])
        #calculate the force using softening potential a  
        for i in range(0, self.dict['n']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            rsquared=dx*dx+dy*dy
            r=np.sqrt(rsquared)
            a1=r*r*r
            a=np.array(a1)
            self.Fx[i]=dx[i]*(1.0/a[i])
            self.Fy[i]=dy[i]*(1.0/a[i])
        return self.Fx, self.Fy
    
    def update(self):
        
        for i in range(0, self.dict['n']):
            y=self.force
             #update particle position
            self.x+=self.dict['dt']*self.vx
            self.y+=self.dict['dt']*self.vy
        
            self.vx+=self.dict['dt']*self.Fx
            self.vy+=self.dict['dt']*self.Fy
        return y
if __name__=='__main__':
    part=particle()
    potential=part.potential()
    #velx=part.update()
    #vely=part.update()
    
    print potential
    
       
       
        
        
    
   
            
            
            
            
