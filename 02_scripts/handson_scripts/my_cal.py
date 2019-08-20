import my_functions
import matplotlib.pyplot as plt
import numpy as np



x = np.arange(20.0)
results =  my_functions.my_functCb(x)

# Writing to files
'''
fh = open('myresults.txt', 'w+')

fh.write("'X', 'Y'\n")

for i in range(len(x)):
    fh.write( "%d %d\r\n" % (x[i], results[i]))
fh.close()
'''

#Reading from files
fh1 = np.genfromtxt('myresults.txt',dtype=float, skip_header=1 ) 

xx = fh1[:,0]
yy = fh1[:,1]
#print(xx)
#print(yy)


plt.plot(xx, yy, marker='o')
plt.title("Plot of $y=x^3$")
plt.xlabel("Int generated from range")
plt.ylabel("Results")
plt.savefig("mycube.png")
plt.show()


