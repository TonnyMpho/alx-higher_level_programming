## JavaScript - Warm up

### Resources

- [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
- [Modern JavaScript Cheatsheet](https://github.com/mbeaudru/modern-js-cheatsheet#modern-javascript-cheatsheet)
- [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Module patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/)

How to Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
[Semi-standard repo](https://github.com/standard/semistandard)

### Tasks

0. script that prints “JavaScript is amazing

1. script that prints 3 lines

2. script that prints a message depending of the number of arguments passed:
	- If no arguments are passed to the script, prints “No argument”
	- If only one argument is passed to the script, prints “Argument found”
	- Otherwise, prints “Arguments found”

3. script that prints the first argument passed to it:
	- If no arguments are passed to the script, print “No argument”

4. script that prints two arguments passed to it, in the following format: “ is ”
```
ubuntu:~$ ./4-concat.js c cool
c is cool
```

5. script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
	- If the argument can’t be converted to an integer, print “Not a number”

6. script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
	- The first line: “C is fun”
	- The second line: “Python is cool”
	- The third line: “JavaScript is amazing”

7. script that prints x times “C is fun”
	- Where x is the first argument of the script
	- If the first argument can’t be converted to an integer, print “Missing number of occurrences”

8. script that prints a square
	- The first argument is the size of the square
	- If the first argument can’t be converted to an integer, print “Missing size”
	- uses the character X to print the square

9. script that prints the addition of 2 integers
	- The first argument is the first integer
	- The second argument is the second integer

10. script that computes and prints a factorial
	- The first argument is integer (argument can be cast as integer) used for computing the factorial
	- Factorial of NaN is 1

11. script that searches the second biggest integer in the list of arguments.
	- can assume all arguments can be converted to integer
	- If no argument passed, print 0
	- If the number of arguments is 1, print 0

12. script to replace the value 12 with 89:

13. function that returns the addition of 2 integers.
