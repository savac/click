# Using 5 different training files, run 5 fold cross validation 
# print training and test error for each epoch and each validation set

from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt
import numpy as np

##############################################################################
# parameters #################################################################
##############################################################################

# A, paths
trainFiles = ['../../data/train_random1on100_1.csv', 
              '../../data/train_random1on100_2.csv',
              '../../data/train_random1on100_3.csv',
              '../../data/train_random1on100_4.csv',
              '../../data/train_random1on100_5.csv']
# B, model
alpha = .1  # learning rate
beta = 1.   # smoothing parameter for adaptive learning rate
L1 = 4.     # L1 regularization, larger value means more regularized
L2 = 1.     # L2 regularization, larger value means more regularized

# C, feature/hash trick
D = 2 ** 28             # number of weights to use
interaction = False     # whether to enable poly2 feature interactions

# D, training/validation
epoch = 5      # learn training data for N passes
#holdafter = None   # data after date N (exclusive) are used as validation
#holdout = None  # use every N training instance for holdout validation
limit= 1e9


##############################################################################
# class, function, generator definitions #####################################
##############################################################################

class ftrl_proximal(object):
    ''' Our main algorithm: Follow the regularized leader - proximal

        In short,
        this is an adaptive-learning-rate sparse logistic-regression with
        efficient L1-L2-regularization

        Reference:
        http://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf
    '''

    def __init__(self, alpha, beta, L1, L2, D, interaction):
        # parameters
        self.alpha = alpha
        self.beta = beta
        self.L1 = L1
        self.L2 = L2

        # feature related parameters
        self.D = D
        self.interaction = interaction

        # model
        # n: squared sum of past gradients
        # z: weights
        # w: lazy weights
        self.n = [0.] * D
        self.z = [0.] * D
        self.w = {}

    def _indices(self, x):
        ''' A helper generator that yields the indices in x

            The purpose of this generator is to make the following
            code a bit cleaner when doing feature interaction.
        '''

        # first yield index of the bias term
        yield 0

        # then yield the normal indices
        for index in x:
            yield index

        # now yield interactions (if applicable)
        if self.interaction:
            D = self.D
            L = len(x)

            x = sorted(x)
            for i in xrange(L):
                for j in xrange(i+1, L):
                    # one-hot encode interactions with hash trick
                    yield abs(hash(str(x[i]) + '_' + str(x[j]))) % D

    def predict(self, x):
        ''' Get probability estimation on x

            INPUT:
                x: features

            OUTPUT:
                probability of p(y = 1 | x; w)
        '''

        # parameters
        alpha = self.alpha
        beta = self.beta
        L1 = self.L1
        L2 = self.L2

        # model
        n = self.n
        z = self.z
        w = {}

        # wTx is the inner product of w and x
        wTx = 0.
        for i in self._indices(x):
            sign = -1. if z[i] < 0 else 1.  # get sign of z[i]

            # build w on the fly using z and n, hence the name - lazy weights
            # we are doing this at prediction instead of update time is because
            # this allows us for not storing the complete w
            if sign * z[i] <= L1:
                # w[i] vanishes due to L1 regularization
                w[i] = 0.
            else:
                # apply prediction time L1, L2 regularization to z and get w
                w[i] = (sign * L1 - z[i]) / ((beta + sqrt(n[i])) / alpha + L2)

            wTx += w[i]

        # cache the current w for update stage
        self.w = w

        # bounded sigmoid function, this is the probability estimation
        return 1. / (1. + exp(-max(min(wTx, 35.), -35.)))

    def update(self, x, p, y):
        ''' Update model using x, p, y

            INPUT:
                x: feature, a list of indices
                p: click probability prediction of our model
                y: answer

            MODIFIES:
                self.n: increase by squared gradient
                self.z: weights
        '''

        # parameter
        alpha = self.alpha

        # model
        n = self.n
        z = self.z
        w = self.w

        # gradient under logloss
        g = p - y

        # update z and n
        for i in self._indices(x):
            sigma = (sqrt(n[i] + g * g) - sqrt(n[i])) / alpha
            z[i] += g - sigma * w[i]
            n[i] += g * g


def logloss(p, y):
    ''' FUNCTION: Bounded logloss

        INPUT:
            p: our prediction
            y: real answer

        OUTPUT:
            logarithmic loss of p given y
    '''

    p = max(min(p, 1. - 10e-15), 10e-15)
    return -log(p) if y == 1. else -log(1. - p)


def data(path, D):
    ''' GENERATOR: Apply hash-trick to the original csv row
                   and for simplicity, we one-hot-encode everything

        INPUT:
            path: path to training or testing file
            D: the max index that we can hash to

        YIELDS:
            ID: id of the instance, mainly useless
            x: a list of hashed and one-hot-encoded 'indices'
               we only need the index since all values are either 0 or 1
            y: y = 1 if we have a click, else we have y = 0
    '''

    for t, row in enumerate(DictReader(open(path))):
        if t<limit:
            # process id
            ID = row['id']
            del row['id']
    
            # process clicks
            y = 0.
            if 'click' in row:
                if row['click'] == '1':
                    y = 1.
                del row['click']
    
            # extract date
            date = int(row['hour'][4:6])
    
            # turn hour really into hour, it was originally YYMMDDHH
            row['hour'] = row['hour'][6:]
            
            row['day'] = str(date%7)
    
            # build x
            x = []
            for key in row:
                value = row[key]
    
                # one-hot encode everything with hash trick
                index = abs(hash(key + '_' + value)) % D
                x.append(index)
    
            yield t, date, ID, x, y

def train(learner, trainFile):
    count = 0;
    for t, date, ID, x, y in data(trainFile, D):  # data is a generator
            p = learner.predict(x)
            learner.update(x, p, y)
            count += 1
    print 'trained on ',count, ' examples from file',trainFile

def getPreds(learner, trainFile):
    for t, date, ID, x, y in data(trainFile, D):  # data is a generator
        p = learner.predict(x)
        yield p,y;
            
def error(learner, trainFile):
    loss = 0;
    count = 0;
    for t, date, ID, x, y in data(trainFile, D):  # data is a generator
            p = learner.predict(x)
            loss += logloss(p, y)
            count += 1
    avgLoss = loss/count;
    return avgLoss;

##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()
print('starting...')

# cross validation
validationErrors =  np.zeros((epoch,5))
trainingErrors = np.zeros((epoch,5))
meanValidationErrors = np.zeros((epoch,))
meanTrainingErrors = np.zeros((epoch,))

#initialize the learners, one learner for each validation set
learner = [ftrl_proximal(alpha, beta, L1, L2, D, interaction) for k in range(5)]

# select validation set
for valSet in xrange(5):
    trainingSets = range(5)
    trainingSets.remove(valSet)

    #train on others
    for e in xrange(epoch):
        trainError = 0;
        for trainSet in trainingSets:
            train(learner[valSet], trainFiles[trainSet])
            trainError += error(learner[valSet], trainFiles[trainSet])/4.0
        validationError = error(learner[valSet], trainFiles[valSet])
        trainingErrors[e,valSet] = trainError;
        validationErrors[e,valSet] = validationError;
        meanValidationErrors[e] += validationErrors[e,valSet] / 5.0;
        meanTrainingErrors[e] += trainingErrors[e,valSet] / 5.0;
        print 'valerror for e=',e,' for valset=',valSet,' n=',validationErrors[e,valSet]
        print 'trainerror for e=',e,' for valset=',valSet,' n=',trainingErrors[e,valSet]

print '//validation errors'
print validationErrors
print '// mean validation errors'
print meanValidationErrors    
print '//training errors'
print trainingErrors
print '// mean training errors'
print meanTrainingErrors
#from matplotlib import pyplot as plt
#plt.figure(1)
#plt.plot(range(epoch), meanValidationErrors, 'bx-')
#plt.plot(range(epoch), meanTrainingErrors, 'rx-')
#plt.show()
#
#plt.figure(2)
#for k in range(5):
#    plt.plot(range(epoch), validationErrors[:,k], 'bx-',label='validation %1.0f'%k)
#    plt.plot(range(epoch), trainingErrors[:,k], 'rx-',label='training %1.0f'%k);
#plt.show()