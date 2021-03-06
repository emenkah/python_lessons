### CODATA 2019 : Introduction to Python programming

Elliot S. Menkah (elliotsmenkah@gmail.com) <br>

## Setting up:

Pythin usually comes pre-installed on linux, however, if you have to install it yourself. This is installed in your system with exclusion.

## Installing Python(2.7) or Python(3.7)

`sudo apt-get install python` or <br>
`sudo apt-get install python3`


## ANACONDA

Anaconda gives you an exclusive environment by keeping all python realted stuff self-contained. If your repositoires is messed up, you can reinstall anaconda and your entire system is not affectd. It also give you the advantage of automatically resolving package dependencies most at times if not or all time. 

Download **anaconda** via the link: 
https://www.anaconda.com/distribution/ and download the **installer** for your respective OS [linux , mac , windows]


### On Anaconda: 
Create an environment  

```bash
conda create <envname>
Eg.
conda create codata 
```

Connect to environment 
```bash
conda activate codata 
```

Installing packages into an environment <br>
```bash
conda install <package> 
Eg.
conda install matplotlib
```

Deactivate/disconnect from present working environment:

```bash
conda deactivate
```

