# Go through filepath, hash features in the same way than the original script
# does, and count how many times hashed features are seen.
# Then output in seenpath 
# - the index of all the (hashed) features seen at least one
# - along with the number of times they have been seen 

from datetime import datetime
from csv import DictReader

filepath = 'data/train_first1e5lines.csv'
seenpath = 'data/seen.csv'

# C, feature/hash trick
D = 2 ** 28             # number of weights to use
interaction = False     # whether to enable poly2 feature interactions

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

    def __init__(self, D, interaction):
        # feature related parameters
        self.D = D
        self.interaction = interaction
        self.seen = [0.] * D

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
        
        #add day%7
        row['day'] = str(date%7)

        # build x
        x = []
        for key in row:
            value = row[key]

            # one-hot encode everything with hash trick
            index = abs(hash(key + '_' + value)) % D
            x.append(index)

        yield t, date, ID, x, y


start = datetime.now()
learner = ftrl_proximal(D, interaction)

for t, date, ID, x, y in data(filepath, D):
    for i in learner._indices(x):
        learner.seen[i] += 1;

with open(seenpath, 'w') as outfile:
    outfile.write('i,seeni\n')
    for i in xrange(len(learner.seen)):
        if learner.seen[i]>0:
            outfile.write('%d,%d\n' %(i, learner.seen[i]))

