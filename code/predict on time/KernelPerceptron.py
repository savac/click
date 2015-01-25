# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 20:08:02 2015

@author: Antoine

Best score seems to be achieved with a polynomial kernel (d=3) although
the performance is poor (~13% error)
"""

# Parameters
epochs = 4;
# Polynomial kernel
c = 1.0;
d = 8.0;
# Gaussian kernel
gamma = 0.001;

from pandas import read_csv;
from numpy import power, transpose, zeros, exp, random, linalg;

def PolynomialKernel(x, t, c, d):
    p = power((c + x.dot(transpose(t))), d);
    return p;
    
def GaussianKernel(x, t, gamma):
    d = x-t;
    return exp(-gamma * d.dot(d));

def LaplacianKernel(x, t, gamma):
    return exp(-gamma * linalg.norm(x-t));

# Load the data set
data = read_csv("../../data/train_hourfixed.csv", header=0, index_col=None, engine='c', usecols=['click', 'hour']);
data = data.ix[random.permutation(data.index)];

y = 2 * data.as_matrix(['click']) - 1; # Scale in {-1,+1}
data = data.as_matrix(['hour']);

# Subsample
validation = data[500:600]
yvalidation = y[500:600];
data = data[1:500];
y = y[1:500];

# Sign function
def Sgn(x):
    return 2 * (x > 0) - 1;

# Prediction
def Predict(weights, data, x, t, kernel, *args):
    conf = 0.0;
    for i in x:
        conf += weights[i] * kernel(data[i], data[t], *args);
        #print("confidence = " + str(conf));
    return Sgn(conf);

# Weights of the perceptron
alpha = zeros(data.size, dtype=float); # Should be sparse if not enough memory
# Memorises exmaples already seen
x = set();

# Training
for k in range(epochs):
    print("Epoch no." + str(1+k))
    mistakes = 0;
    for i in range(data.size):
        #print("alpha = " + str(alpha))
        yhat = Predict(alpha, data, x, i, LaplacianKernel, gamma);
        if yhat != y[i]:
            alpha[i] += y[i];
            x |= set([float(i)]);
            mistakes += 1;
    print(str(mistakes) + " mistakes.");

# Validation
yhat = zeros((validation.size,1));
for i in range(validation.size):
    yhat[i] = Predict(alpha, data, x, i, LaplacianKernel, gamma);
            
Error = sum(yhat != yvalidation) / validation.size;
print(Error);
