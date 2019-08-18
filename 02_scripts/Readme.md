# Python lessons - CODATA-RDA 2019 - Scripts 

* Functions in python script
    + "\_\_name\_\_" in scripts
    + Modules
    + Type casting when reading from argv
* Read and writing to files
* More numpy and python operations
* Numerics formating


[Simple Script](https://github.com/emenkah/python_lessons/tree/master/02_scripts/my_functions0.py) 

```python
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
a=2
b=5

res0 = my_square(a,b)
res1 = my_addition(a,b)
res2 = my_subtraction(a,b)
res3 = my_div(a,b)
```
Results:

```bash
Square of sum of 'a' and 'b' is 49
Sum of 'a' and 'b' is 7
Difference between  2 and  5 is -3
A division of 2 by 5 is:  0.4

```

```python

if __name__ == '__main__' :
    var = cast(sys.argv[1])
```

cast to integers: int(sys.argv[i]) <br>
cast to floats: float(sys.argv[i]) <br>
