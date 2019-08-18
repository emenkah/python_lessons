
import numpy as np
import sys

import my_functions0

def my_cubeFunction(x):
    ''' 
        Function that spwans a list/array of numbers or a vector and comutes the cude of the the respective vector elements
    '''
    xx = np.array(range(1,x))
    y = xx ** 3

    #print("Computing the cude of", len(xx) ,"numbers \n")

    # Open file to write to 
    fh = open("my_res.txt", "w+")

    # Write header of file
    fh.write('"X"' ", " '"Y"\n')

    for i in range(len(xx)):

        fh.write( "%d %d\r\n" % (xx[i], y[i]))

    return y


if __name__ == '__main__' :
    
    num = int(sys.argv[1])
    print("It is {}".format(__name__))
    print("Runing my script with {}".format(num))
    res = my_cubeFunction(num)
    
else:
    num = 30
    print("It is {}".format(__name__))
    print("Runing my script with {}".format(num))
    res = my_cubeFunction(num)
#fh = open("my_res.txt", "a")



print("Total No of arguments", len(sys.argv))
#print("Path of WD: ", sys.path)
