import numpy as np

########################################################################
# Each line of the data set contains one (xn, yn) with xn belone to R^4.
# The first 4 number of the line contains the components of xn orderly.
# And the last numer is yn. Please initialize your algorithm with w=0 and
# take sign(0)=-1. Please always remember to add x0=1 to each xn. Implement 
# a version of PLA by visiting examples in the naive cycle using the order 
# of examples in the data set.
##########################################################################

# load data set
data = np.loadtxt("hw1_15_train.dat.txt")

# initialization
w = [0.0, 0.0, 0.0, 0.0, 0.0]   # weight vector of g0
x = [1.0] 
s = 0


# set sign()
def sign(x):
    if x > 0:
        return 1
    else:
        return -1

# Cyclic PLA algorithm
end = 0     # check the cycle
count = 0   # record the number of updates
i = 0       # point to the current data
x = 5*[1.0] # make x list initialize all 1.0

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
print(count)
    
    




    