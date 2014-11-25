import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

def parseFile(file):
    file = open(file, 'rU')
    adjFile = csv.reader(file, delimiter=',')    
    matrix = []
    for row in adjFile:
        a = []
        for entry in row:
            a.append(float(entry))
        matrix.append(a)
    return matrix

def PCA(matrix, s):

    matrix = np.matrix(matrix) * np.matrix(matrix).transpose()
    print matrix
    U,S,V = np.linalg.svd(matrix)

    print 'U:\n'
    print U

    E = np.matrix(np.diag(S))
    U = np.matrix(U)

    W = U * E
    
    W = W[:,0:s]

    return W, S

matrix = parseFile('seeds_dataset.csv')
W, S = PCA(matrix, 2)
print 'W:\n'
print W
