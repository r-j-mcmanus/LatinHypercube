

import numpy as np
import random



class Sampler(object):
	def __init__(self, n_dim, n_sample):
		"""
		Sampler class
		-------------
		Arguments
		---------
		n_dim    --- The number of simentions we draw from
		n_sample --- The number of points drawn

		Functions
		---------
		setInterval --- will set the interval for a dimention or 
						for all dimentions.
		getPoints   --- will run the algorithem and return points

		Explination
		-----------
		Will return points following the Latin?Hypercube method.

		This is where each axis is split into n_sample strata and 
		a point is chosten at random within the n_sample*n_dim 
		strata. One found, points are found from poping a result
		a random from each strata for each dimention.

		To set the range of each dimention, use setInterval
		To get the points according to the algorithm use getPoints
		"""
		self.n_dim = n_dim
		self.intervals = [[0,1] for i in range(n_dim)]
		self.n_sample = n_sample

	def __devider(self, dim):
		points = [ 0 for i in range(self.n_sample) ]
		dx = ( self.intervals[dim][0] - self.intervals[dim][1] ) / self.n_sample
		for i in range(self.n_sample):
			points[i] = ( random.uniform(0, 1) + i ) * dx
		return points

	def setInterval(self, lower, upper, dim = 0):
		"""
		Arguments
		---------
		lower --- the lower value drawn from
		upper --- the upper value drawn from
		dim   --- (optional) if 0 will use lower and upper for all
				  dimentions. Otherwise will set for the dimention
				  given
		"""
		if dim != 0:
			self.intervals[dim][0] = lower
			self.intervals[dim][1] = upper
		else:
			for i in range(self.n_dim):
				self.intervals[i][0] = lower 

	def getPoints(self):
		pointsFromStrata =  [
			self.__devider(dim) for dim in range(self.n_dim)
		]

		points = [
			[
				pointsFromStrata[i].pop(random.randint(0, j)) for i in range(self.n_dim) 
			]
			for j in reversed(range(self.n_sample)) 
		]

		return np.array(points)

sampler = Sampler(2, 5)
sampler.setInterval(0, 5)
print sampler.getPoints()

