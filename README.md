# cookie-login 

Cookie Login is a Python script for logging into websites using HTTP Cookies and Requests. It allows you to login to various websites using your existing account and store the authentication cookies for future use.
## Installation

1. Clone the repository to your local machine using Git:

```bash
git clone https://github.com/xcoders-teams/cookie-login
```

2. Change into the cookie-login directory:

```bash
cd cookie-login
```

3. Install the required packages using pip:
```bash
pip install -r requirements.txt
```
## Usage

1. Run the script using the following command:

```python
python Run.py
```

2. Enter the URL of the website you want to log in to when prompted.
3. Enter your username or email and password when prompted.

4. The script will attempt to log in to the website using the provided credentials and print the result to the console.

5. If the login is successful, the script will save the HTTP cookies to a file named success_cookies.txt in the result directory.

6. If the login fails, the script will save the HTTP cookies to a file named failed_cookies.txt in the result directory.
## Authors

- [@hans](https://www.github.com/hansalr)
- [@Fxc7](https://www.github.com/Fxc7)
## Contributing

Contributions are always welcome!
See `README.md` for ways to get started.
Please adhere to this project's `code of conduct`.
## License

[GNU](https://www.gnu.org/licenses/why-not-lgpl.html)