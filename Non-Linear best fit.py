"""
Figures out how to find correlation and line of best fit on non linear
patterns of data and thier modeled functions.
This file displayes it on three examples.
"""

import numpy as np
import matplotlib.pyplot as plt

step = 1
threshold = 1


# Ex 1: two regions where y is 2x
x = np.random.uniform(0, 10, [500])
y = np.random.uniform(3, 10, [500])

for i in range(500):
	if x[i] > 7 or x[i] < 3:
		y[i] = y[i]*2

dataset1 = [x, y]

# Ex 2: y = x + random factor until 5 then y = 10 - x + random factor
x = np.random.uniform(0, 10, [500])
y = np.zeros(500)

for i, c in enumerate(x):
	random_factor = np.random.uniform(0, 5, 1)
	if np.random.randint(0, 1, 1):
		random_factor = -random_factor
	if c <= 5:
		y[i] = c + random_factor
	else:
		y[i] = 10 - c + random_factor

dataset2 = [x, y]


# Ex 3: y = sin 1.5x + random factor

x = np.random.uniform(0, 10, [500])
y = np.zeros(500)

for i, c in enumerate(x):
	random_factor = np.random.uniform(0, 5, 1)
	if np.random.randint(0, 1, 1):
		random_factor = -random_factor

	y[i] = np.sin(2*c) + random_factor

dataset3 = [x, y]


def find_best_fit(fx, fy, plot=True):
	# graph x:fx, y:fy then use to find mean at curr xpoint and assemble line

	pointx = np.array([])
	pointy = np.array([])

	# loop through data by step
	for xpoint in range(int(min(fx)), int(max(fx)) + 1, step):

		# find all points within threshold
		w = np.where(np.all([(xpoint + threshold) >= fx, fx >= (xpoint - threshold)], axis=0))

		# find y for this step
		if len(np.unique(w, return_counts=True)[0]) > 1:
			point1y = fy[w].mean()
		else:
			index = (np.abs(fx - xpoint)).argmin()
			point1y = fy[index]


		# store data
		pointx = np.append(pointx, xpoint)
		pointy = np.append(pointy, point1y)

	#reshape
	pointx = pointx.reshape(pointx.size)
	pointy = pointy.reshape(pointx.size)

	# sorted format for graphing
	sidx = np.argsort(pointx)

	# data for refrence
	plt.scatter(fx, fy)

	#line
	plt.plot(np.take_along_axis(pointx, sidx, 0), np.take_along_axis(pointy, sidx, 0))

	plt.show()


# show data
plt.scatter(dataset1[0], dataset1[1])
plt.show()
# show best fit line for that data
find_best_fit(dataset1[0], dataset1[1])

plt.scatter(dataset2[0], dataset2[1])
plt.show()

find_best_fit(dataset2[0], dataset2[1])

plt.scatter(dataset3[0], dataset3[1])
plt.show()

# adjust threshold for more delicate data
threshold = .5
find_best_fit(dataset3[0], dataset3[1])
