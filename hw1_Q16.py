import numpy as np
import random

########################################################################
# Implement a version of PLA by visiting examples in fixed, pre-determined
# random cycles throughout the algorithm. Run the algorithm on the data set.
# Please repeat your experiment for 2000 times, each with a different 
# random seed. What is the average number of updates before the algorithm halts?
##########################################################################

# load data set
data = np.loadtxt("hw1_15_train.dat.txt")
   
# set sign()
def sign(x):
    if x > 0:
        return 1
    else:
        return -1

# Cyclic PLA algorithm
def PLA(r):
    w = 5*[0.0]  # weight vector of g0
    end = 0      # check the cycle
    count = 0    # record the number of updates
    i = r        # point to the current data
    x = 5*[1.0]  # make x list initialize all 1.0
    while end < len(data)-1:
        x[1:5] = data[i][0:4]                       # replace vector x with data
        if sign(np.dot(w, x)) != data[i][-1]:       # find mistake
            y = 5*[data[i][-1]]                     
            w += np.multiply(y, x)                  # update w to correct mistake
            end = 0
            count = count + 1
        i = i+1
        end = end+1
        if i>=len(data):
            i=0
    return count

result = list()
for i in range(0, 2000):
    r = random.randint(0, len(data)-1)
    result.append(PLA(r))

print(np.mean(result))



    
    




    