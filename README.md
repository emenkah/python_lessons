# Python lessons
Python Lessons

Launch the python intepreter by running the command **python** <br>

**Eg**: <br>
`(base) user@hp6g4-inf-36:~$ python` <br>
`[GCC 7.3.0] :: Anaconda, Inc. on linux` <br>
`Type "help", "copyright", "credits" or "license" for more information. `<br>
`>>> `
<br>

You can close the intepreter or leave the python environemt by the `exit` command: <br>
`>>> exit()`

#### Relaunch python intepreter by running the command `**python**` <br>
`(base) user@hp6g4-inf-36:~$ python` <br>

### Print functions and strings:

`>>> print("Hello World") ` <br>
    `Hello World`  <br>
<!--`>>> print('Holla Mundo')` -->
<br>
<br>
`>>> print("We're here")` # Rather use <span style="color:blue">double outer quotes</span>  over single outter quotes <br>
`We're here` <br>
`>>> print('We\'e here')` # <span style="color:red">Avoid complications</span>. <br>
`We're here` <br>

### Concatenation of Strings
`>>> print("Hi" + " there")` <br>
`Hi there`

### Variable assignement: 
#Variables take on the **data type** of the values being assigned to them.

`>>> var0 = 7` <br>
`>>> var1 = 5.2` <br>
`>>> var2 = "hello"` <br>
`>>> var3 = True` <br>


#### Integer Variable:  
`>>> print(var0)` <br> 
` 7 ` <br>
`>>> type(var0)` <br>
` <type 'int'>` <br>

#### Floating point Variable:  
`>>> print(var1)` <br>
` 5.2 ` <br>
`>>> type(var1)` <br>
`<type 'float'>` <br>

#### String Variable:  
`>>> print(var2)` <br>
`hello` <br>
`>>> type(var2)` <br>
`<type 'str'>` <br>

#### Boolean Variable:  
`>>> print(var3)` <br>
`True` <br>
`>>> type(var3)` <br>
`<type 'bool'>` <br>

`>>> print(var1, var2, var3 )` <br>
`(5.2, 'hello', True)` <br>


### List, tuples and loops:




`>>> y = ["Hey", "you", 5, 8.7]` # <span style="color:blue">List</span> <br>
<br>
`>>> x = ("hello", "hi", "you")`  # <span style="color:green">Tuple</span> ( It's an immutable <span style="color:blue">List</span> ) <br>
same as:
`>>> x = "hello", "hi", "you"` <br>

`>>> z = [2, 3, 4, 5, 6]` <br>

`>>> print(type(x))` <br>
`<type 'tuple'>` <br>
`>>> print(type(y))` <br>
`<type 'list'>`


Memory locations for storing data in list and tuples are indexed so one could access data stored in a specific memory loactions: **NB**: By default, index locations begin from zero (0)

`>>> num0 = z[0]` <br>
`>>> print(num)` <br>
2

### Loops ( for and while ): "range & len" functions
##### Use of the **range** function

Prints out the elements of the list "z" <br>
`>>> for i in z:` <br>
`...     print(i)` <br>

#### Range & Len functions
`>>> range(4)` <br>
`[0, 1, 2, 3]` <br>

`>>> len(y)` ## From the list  y = ["Hey", "you", 5, 8.7] <br> 
`4` <br>

Prints out the lenght of the list "z" <br>
`>>> len(z)` <br>
`5`

`>>> range(len(z))` <br>
`[0, 1, 2, 3, 4]`


    

Combine range and len to use in for loops. The code below should print the elements of the [list z] to screen

`>>> for i in range(len(z)):` <br>
`...     print(z[i]) `

##### While loop


i = 0 <br>
`>>> while i < 3`: <br>
`...     i = i + 1` <br>
`...     print(z[i])`<br>

## Modules

There are enormous libraries in python that can be imported to use rather than having to build your own. This make life much easier.

**`math`** is one of many libraries that requires that you import in order to use it.

### Importing with 'import'

`>>> import math` # This imports all symbols(functions and variables) in the module into the current namespace.

### Looking at what a module contains, and its documentation  <br>

#### Funtions and variables: <br>
Once a module is imported, you can list the symbols it provides using the `dir`
function : <br>

`>>> print(dir(math))` 

`['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']`

<br>
#### Documentation: <br>
You can also query look at the the module's documentations or a symbol's documentation using the `help`
function : <br>
`>>> help(math)` <br>
`>>> help(math.log)` <br>

We can chose to import all symbols (functions and variables) in a
module to the current namespace (so that we don't need to use the prefix
"`math.`" every time we use something from the `math` module:


