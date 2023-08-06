import matplotlib.pyplot
import numpy
data = numpy.array([45, 25, 15, 12, 8])
labels = ["p", "z", " l", "a", "k"]
matplotlib.pyplot.pie(data, labels = labels, shadow= True)
matplotlib.pyplot.show()