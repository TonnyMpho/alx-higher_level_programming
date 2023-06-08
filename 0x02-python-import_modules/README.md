## 0x02. Python - import & modules

### Tasks

#### 0. Import a simple function from a simple file

##### A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

#### 1. My first toolbox!

##### A program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

* Do not use the function print (with string format to display integers) more than 4 times
* Have to define:
* the value 10 to a variable a
* the value 5 to a variable b
* and use those two variables only, as arguments when calling functions (including print)

#### 2. How to make a script dynamic!

##### A program that prints the number of and the list of its arguments.

* The output should be:
* Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
* : (or . if no arguments were passed) followed by
* a new line, followed by (if at least one argument),
* one line per argument:
* the position of the argument (starting at 1) followed by :, followed by the argument value and a new line

#### 3. Infinite addition

##### A program that prints the result of the addition of all arguments

* The output should be the result of the addition of all arguments, followed by a new line
* Cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
* Code should not be executed when imported

#### 4. Who are you?

##### A program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

* should print one name per line, in alpha order
* should print only names that do not start with __
* Code should not be executed when imported
* Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)

#### 5. Everything can be imported

##### A program that imports the variable a from the file variable_load_5.py and prints its value.

* Not allowed to use * for importing or __import__
* Code should not be executed when imported
