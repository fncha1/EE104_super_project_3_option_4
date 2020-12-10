# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 03:55:25 2020

@author: project 4 group 5
"""

#to load  the cifar10 dataset
from matplotlib import pyplot
from tensorflow.keras.datasets import cifar10
# load dataset
(trainX, trainy), (testX, testy) = cifar10.load_data()
# summarize loaded dataset
print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
print('Test: X=%s, y=%s' % (testX.shape, testy.shape))
# plot first few images
for i in range(9):
	# define subplot
	pyplot.subplot(330 + 1 + i)
	# plot raw pixel data
	pyplot.imshow(trainX[i])
# show the figure
pyplot.show()