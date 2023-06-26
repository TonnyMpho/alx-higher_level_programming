## 0x05. Python - Exceptions

### Tasks

#### 0. Safe list printing

##### Function that prints x elements of a list.

##### Prototype: def safe_print_list(my_list=[], x=0):
* my_list can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* x represents the number of elements to print
* x can be bigger than the length of my_list
* Returns the real number of elements printed
* Have to use try: / except:
* Not allowed to import any module
* Not allowed to use len()

#### 1. Safe printing of an integers list

##### unction that prints an integer with "{:d}".format().

##### Prototype: def safe_print_integer(value):
* value can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns True if value has been correctly printed (it means the value is an integer)
* Otherwise, returns False
* Have to use try: / except:
* Have to use "{:d}".format() to print as integer
* not allowed to import any module
* not allowed to use type()

#### 2. Print and count integers

##### function that prints the first x elements of a list and only integers.

##### Prototype: def safe_print_list_integers(my_list=[], x=0):
* my_list can contain any type (integer, string, etc.)
* All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
* x represents the number of elements to access in my_list
* x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
* Returns the real number of integers printed
* have to use try: / except:
* have to use "{:d}".format() to print an integer
* not allowed to import any module
* not allowed to use len()

#### 3. Integers division with debug

##### function that divides 2 integers and prints the result.

##### Prototype: def safe_print_division(a, b):
* You can assume that a and b are integers
* The result of the division should print on the finally: section preceded by Inside result:
* Returns the value of the division, otherwise: None
* You have to use try: / except: / finally:
* You have to use "{}".format() to print the result
* You are not allowed to import any module

#### 4. Divide a list

##### Write a function that divides element by element 2 lists.

##### Prototype: def list_division(my_list_1, my_list_2, list_length):
* my_list_1 and my_list_2 can contain any type (integer, string, etc.)
* list_length can be bigger than the length of both lists
* Returns a new list (length = list_length) with all divisions
* If 2 elements can’t be divided, the division result should be equal to 0
* If an element is not an integer or float:
* print: wrong type
* If the division can’t be done (/0):
* print: division by 0
* If my_list_1 or my_list_2 is too short
* print: out of range
* You have to use try: / except: / finally:
* You are not allowed to import any module

#### 5. Raise exception

##### Write a function that raises a type exception.

##### Prototype: def raise_exception():
* You are not allowed to import any module

#### 6. Raise a message

##### Write a function that raises a name exception with a message.

##### Prototype: def raise_exception_msg(message=""):
* You are not allowed to import any module
