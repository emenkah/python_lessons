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


