import sys



def my_square(a,b):
    y = (a +b ) ** 2
    print("Square of sum of 'a' and 'b' is",y)
    return y

def my_addition(a,b):
    y = (a + b)
    print("Sum of 'a' and 'b' is",y)
    return y

def my_subtraction(a,b):
    y = a-b 
    print("Difference between ", a, "and ", b, "is", y)
    return y


def my_div(a,b):
    y = a/b
    print("A division of", a, "by",b, "is: ", y)
    return y

# Assigninng variables 

if __name__ == '__main__' :
    
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    res0 = my_square(a,b)
    res1 = my_addition(a,b)
    res2 = my_subtraction(a,b)
    res3 = my_div(a,b)

