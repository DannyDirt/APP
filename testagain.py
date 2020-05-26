#this is my test for github

import numpy as np

a = np.array(list(range(6)))
a = a.reshape(2,3)
print(a)

b = np.array(list(range(12)))
b = b.reshape(3,4)
print(b)

c = a.dot(b)
print(c)