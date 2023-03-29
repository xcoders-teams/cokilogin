setup(
    name='cookie-login',
    version='0.1.0',
    description='A Python script for logging into websites using HTTP Cookies and Requests',
    long_description='cookie login is a Python script that allows you to log into various websites using HTTP Cookies and Requests. It can be used to automate logging into websites that require authentication for scraping data, monitoring or other purposes. With a simple command-line interface, you can easily specify the website URL, login credentials and save the cookies for later use.',
    author='xcoders teams',
    author_email='farhanxcode7@api-xcoders.site',
    url='https://github.com/xcoders-teams/cookie-login',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyyaml'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'cookie-login = cookie-login.__main__:main'
        ]
    }
)