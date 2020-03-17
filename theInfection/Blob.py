
from  random import *

class blob:
	def __init__(self,r,thickness,spawn,speed,limit):
		self.x = spawn[0]
		self.y = spawn[1]
		self.xlimit = (r+thickness,limit[0]-(r+thickness))
		self.ylimit = (r+thickness,limit[1]-(r+thickness))
		self.position = (self.x, self.y)
		self.radius = r
		self.thickness = thickness
		self.speed_x =speed[0]*choice([-1,1])
		self.speed_y =speed[1]*choice([-1,1])
		self.infected = False
		self.immunizer = False
		self.color = [0,255,0]


	def update(self):

		# Bounce back from the edges by reversing the spped of x and y
		if self.x <= self.xlimit[0] or self.x >=self.xlimit[1]:
			self.speed_x  = self.speed_x*-1
		if self.y <= self.ylimit[0] or self.y >= self.ylimit[1]:
			self.speed_y  = self.speed_y*-1

		# update the co-ordinates
		self.x += self.speed_x
		self.y += self.speed_y
		self.position  = (self.x,self.y)
		if self.infected:
			self.color = [0,0,255]
		else:
			self.color = [0, 255, 0]
		if self.immunizer:
			self.color= [255,0,0]


	def __sub__(self, other):
		# returns the distance from other blob

		return int( ((self.x-other.x)**2 + (self.y-other.y)**2 )**(1/2))



