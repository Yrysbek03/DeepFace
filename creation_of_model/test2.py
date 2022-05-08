import numpy

arr = numpy.array([[250, 250, 250, 255], [250, 250, 250, 255], [250, 250, 250, 255]])
for i in arr:
    print(numpy.array(i).mean(dtype='int'))
