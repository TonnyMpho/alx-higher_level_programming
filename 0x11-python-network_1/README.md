## 0x11. Python - Network #1#### Resources

#### Read:

- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with requests package](https://requests.readthedocs.io/en/latest/)
- [requests package](https://pypi.org/project/requests/)

### Tasks

0. What's my status? #0

#### Python script that fetches `https://alx-intranet.hbtn.io/status`

- must use the package `urllib`
- not allowed to import any packages other than `urllib`
- must use a `with` statement

1. Response header value #0

#### Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- must use the packages `urllib` and `sys`
- not allow to import packages other than `urllib` and `sys`
- don’t need to check arguments passed to the script (number or type)
- must use a `with` statement

2. POST an email #0

#### Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

- The email must be sent in the `email` variable
- must use the packages `urllib` and `sys`
- not allowed to import packages other than `urllib` and `sys`
- don’t need to check arguments passed to the script (number or type)
- must use the `with` statement

3. Error code #0

#### Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
- must use the packages `urllib` and `sys`
- not allowed to import other packages than `urllib` and `sys`
- don’t need to check arguments passed to the script (number or type)
- must use the `with` statement

4. What's my status? #1

#### Python script that fetches `https://alx-intranet.hbtn.io/status`

- must use the package `requests`
- not allowed to import packages other than `requests`

5. Response header value #1

#### Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

- must use the packages `requests` and `sys`
- not allow to import other packages than `requests` and `sys`
- The value of this variable is different for each request
- don’t need to check script arguments (number and type)

6. POST an email #1

#### Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email must be sent in the variable `email`
- must use the packages `requests` and `sys`


7. Error code #1

#### Python script that takes in a URL, sends a request to the URL and displays the body of the response.

- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- must use the packages `requests` and `sys`

8. Search API

- #### Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
##### Otherwise:
- Display `Not a valid JSON` if the JSON is invalid
- Display `No result` if the JSON is empty
- must use the package `requests` and `sys`

##### Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users?apiVersion=2022-11-28) to display your `id`

- must use [Basic Authentication](https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api?apiVersion=2022-11-28) with a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) as password to access to your information (only read:user permission is needed)
- first argument will be your `username`
- The second argument will be your `password` (in your case, a personal access token as password)
- must use the package ``requests`` and ``sys``


##### Copyright © 2023 ALX, All rights reserved.
