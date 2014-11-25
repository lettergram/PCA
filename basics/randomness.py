"""
  Generate a graph of random points
  Written for http://austingwalters.com
  Written by Austin G. Walters
  Date: 11/25/2014 Python 2.7
"""
import numpy as np
import matplotlib.pyplot as plt

def genRandomGauss(s, mu, sigma, area, colors):
    
    x = np.random.normal(mu, sigma, s)
    y = np.random.normal(mu/2, sigma/4, s)
    y = y + x/2
    colors = np.random.rand(s)
    area = np.pi * 2
    plt.scatter(x, y, s=area, c=colors)
    plt.title('Gaussian Distrabution')
    plt.axis([-60, 60, -60, 60])
    plt.show()
    
    return x, y

def reduceDim(s, x, y, area, colors):
    removeY = [0] * s
    plt.scatter(x, removeY, s=area, c=colors)
    plt.axis([-60, 60, -60, 60])
    plt.title('X dimension')
    plt.show()

    removeX = [0] * s
    plt.scatter(removeX, y, s=area, c=colors)
    plt.axis([-60, 60, -60, 60])
    plt.title('Y dimension')
    plt.show()


def normalized(s, x, y, area, colors):

    x -= x.mean(axis=0)
    y -= y.mean(axis=0)

    plt.scatter(x, y, s=area, c=colors)
    plt.axis([-60, 60, -60, 60])
    plt.title('normalized')
    plt.show()

    return x, y

def PCA(matrix, s):

    
    matrix = np.matrix(matrix) * np.matrix(matrix).transpose()
    U,S,V = np.linalg.svd(matrix)
    E = np.sqrt(np.matrix(np.diag(S)))
    U = np.matrix(U)

    W = U * E    

    x = np.array(W[0,:])[0]
    y = np.array(W[1,:])[0]

    plt.scatter(x, y, s=area*10, c=colors)
    plt.axis([-60, 60, -60, 60])
    plt.title('normalized')
    plt.show()

    return W

s = 1000
colors = np.random.rand(s)
area = np.pi * 2
x, y = genRandomGauss(s, 10, 20, area, colors)
normalized(s, x, y, area, colors)
reduceDim(s, x, y, area, colors)
W = PCA(np.vstack([x, y]).transpose(), 5)
