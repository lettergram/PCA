import os
import struct
import numpy as np

import matplotlib
import matplotlib.mlab as mlab
from matplotlib import pyplot
import matplotlib as mpl
 
"""
Read taken from http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py
This is only to read the data
which is GPL licensed.
"""
def read(dataset = "training", path = "."):
    """
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
    """
 
    if dataset is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError, "dataset must be 'testing' or 'training'"
 
    # Load everything in some numpy arrays
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)
 
    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(len(lbl), rows, cols)
 
    get_img = lambda idx: (lbl[idx], img[idx])
 
    # Create an iterator which returns each image in turn
    for i in xrange(len(lbl)):
        yield get_img(i)

"""
  Displays output images
"""
def show(image):
    fig = pyplot.figure()
    ax = fig.add_subplot(1,1,1)
    imgplot = ax.imshow(image, cmap=mpl.cm.Greys)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
    pyplot.show()

"""
  My method of training
"""
def train(d, attrCount):
    matrix = []
    count = []
    test = []
    u = []
    sigma = []
    for i in range(10):
        matrix.append(0)
        count.append(0)
    d = read()
    for img in d:
      
        # Subtract mean
        m = np.subtract(img[1], np.mean(img[1]))
        
        if count[img[0]] is 0:
            matrix[img[0]] = np.reshape(m, -1).T
            count[img[0]] = 1

        if count[img[0]] < 100:
            count[img[0]] += 1
            centered = np.reshape(m, -1).T
            matrix[img[0]] = np.vstack((matrix[img[0]], centered))

        else:
            test.append(img)
    b = 0
    for num in matrix:
      
          pca = (mlab.PCA(num.T, standardize=False)).Y.T
          pca = pca[0:attrCount]

          show(np.cov(pca.T))

          sigma.append(np.cov(pca.T))
          u.append([])
          for i in range(attrCount):
              u[b].append(np.mean(pca[i]))
          b += 1

    return u, sigma, test


u, sigma, test = train(read(), 30)

right = 0.0
total = 0.0
for img in test:
  
    matrix = np.subtract(img[1], np.mean(img[1])) # Center
    matrix = np.reshape(matrix, (-1, 1))
    covImg = np.dot(matrix, np.reshape(matrix, (1, -1))).T
    
    index = 0;
    best = 0.0
  
    for i in range(10):
      if best < np.mean(covImg * sigma[i]):
          index = i
          best = np.mean(covImg * sigma[i])
    if img[0] == index:
        right += 1.0

    total += 1.0
    print (right/total), total, img[0], index

print right
print total
print "accuracy", right/total
