#cg1.	Create a one dimensional array with the following values 1, 4, 3 and print the values

import numpy as np


dma = np.array([1,4,3])
print(dma)
'''
print(type(dma.data))
print(type(dma.shape))
print(type(dma.dtype))
print(type(dma.strides))
'''

dma2 = np.array([(1, 2, 3), (4, 5, 6)])
print(dma2) 
print(type(dma2))

