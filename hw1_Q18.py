import numpy as np
import random
import time
########################################################################
# Modify your PLA in Question 16 to visit examples purely randomly, and 
# then add the "pocket" steps to the algorithm. Use training set as D, and 
# testing set for verifying the g returned by your algorithm. The sets are 
# of the same format as the previous one. Run the pocket algorithm with a 
# total of 50 updates on D, and verify the performance of wpocket using the 
# test set. Please repeat your experiment for 2000 times, each with a 
# different random seed. What is the average error rate on the test set?
##########################################################################

# load data set
data = np.loadtxt("hw1_18_train.dat.txt")
test = np.loadtxt("hw1_18_test.dat.txt")

# set sign()
def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def verify(w):
    avg = 0
    x = 5*[1.0]
    for i in range(0, len(test)):
        x[1:5] = test[i][0:4]
        if sign(np.dot(w, x)) != test[i][-1]:
            avg = avg+1   # wrong 
    return float(avg/len(test))

# Cyclic PLA algorithm
def PLA(r):
    w = 5*[0.0]   # weight vector of g0
    count = 0     # record the number of updates
    i = r         # point to the current data
    x = 5*[1.0]   # make x list initialize all 1.0
    error_w = verify(w)
    while True:
        x[1:5] = data[i][0:4]                       # replace vector x with data
        if sign(np.dot(w, x)) != data[i][-1]:       # find mistake
            y = 5*[data[i][-1]]                     
            w = w + np.multiply(y, x)
            error_update = verify(w)
            if error_update<error_w:
                error_w = error_update
            count+=1

        i = i+1
        if i == r:
            return error_w
        if count >= 50:
            return error_w
        if i>=len(data):
            i = 0

result = list()
for i in range(0, 2000):
    r = random.randint(0, len(data)-1)
    result.append(PLA(r))

print(np.mean(result))

