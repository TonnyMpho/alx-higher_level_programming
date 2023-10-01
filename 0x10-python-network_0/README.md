## 0x10. Python - Network #0

#### Read:

- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

- All Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All files must be executable
- The first line of all your bash files should be exactly #!/bin/bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option -s (silent mode)


### Tasks

0. cURL body size

- #### Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- have to use `curl`

    
1. cURL to the end

- #### Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

	- Display only body of a `200` status code response
	- have to use `curl`
    
2. cURL Method

- #### Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response

	- have to use `curl`

    
3. cURL only methods

- #### Bash script that takes in a URL and displays all HTTP methods the server will accept.

	- have to use `curl`
    
4. cURL headers

- #### Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response

	- A header variable `X-School-User-Id` must be sent with the value `98`
	- have to use `curl`
    
5. cURL POST parameters

- #### Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

	- A variable `email` must be sent with the value `test@gmail.com`
	- A variable `subject` must be sent with the value `I will always be here for PLD`
	- have to use `curl`
    
6. Find a peak

- Technical interview preparation:

- not allowed to google anything
- Whiteboard first

- #### Write a function that finds a peak in a list of unsorted integers.

	- Prototype: def find_peak(list_of_integers):
	- not allowed to import any module
	- algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
	- 6-peak.py must contain the function
	- 6-peak.txt must contain the complexity of your algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`
__Note__: there may be more than one peak in the list

    
7. Only status code

- #### Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

	- not allowed to use any `pipe`, `redirection`, etc.
	- not allowed to use `;` and `&&`
	- have to use `curl`

    
8. cURL a JSON file

- #### Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.

	- script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
	- have to use `curl`
    
9. Catch me if you can!

- #### Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.

	- have to use `curl`
	- not allowed to use `echo`, `cat`, etc. to display the final result
