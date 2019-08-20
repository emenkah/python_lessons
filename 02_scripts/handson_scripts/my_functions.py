import numpy as np
import sys


def my_functCb(varx):
	vary =  varx ** 3 
	return vary

def my_functSq(varx):
	vary =  varx ** 2 
	return vary


print(__name__)
if __name__ == '__main__':

    r = int(sys.argv[1])

    var0 = np.arange(r)

    res0 = my_functCb( var0)

    res1 = my_functSq( var0)

