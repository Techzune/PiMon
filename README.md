# PiMon
Designed for Mississippi State University IEEE SECON Robotics team in Software Engineer Senior Project 2019.
Provides a web interface to view robot diagnostics data.


## Authors
Spencer Barnes, Jake Griesmer, Jordan Stremming, Tyler Whiticker


## Installation
This project uses **Python 3.7** and the **pipenv** package.
To install Pipenv, run `pip3 install pipenv`.

Clone this repository into a folder of your choosing and run
`pipenv install`. This will install all necessary packages for this project.


## Development
PiMon is developed with the following:
* Python 3.7 + pipenv
* Bootstrap 4.3.1 + Bootswatch (Darkly)
* Flask
* Apache2 + modWSGI

You may need C++ Build Tools to install all packages.

## Usage
#### Running via WSGI
Configure your web server to launch the application via pimon.wsgi.
PiMon was developed with Apache2.

[Click here for more information via modWSGI's wiki.](https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html)
