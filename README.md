# PiMon
Designed for the Mississippi State University IEEE SECON Robotics team in Software Engineer Senior Project 2019-2020
Provides a web interface to view robot diagnostics data.


## Authors
Spencer Barnes, Jake Griesmer, Jordan Stremming, Tyler Whiticker, Dylan Santa Cruz, Will Storey


## Installation

### Dependancies
On the Pi:
* Python3.7
* Pipenv for python3
* Redis server
* SerialManager process _[GitHub here](https://github.com/MSUSeconRobotics/SerialManager.git)_

On the Arduino:
* NewPing.h _Available in Arduino Library Manager_
* JsonSerialStream.h _[GitHub here](https://github.com/MSUSeconRobotics/JsonSerialStream)_

### Installation Instruction
To install Pipenv, run `pip3 install pipenv`.

Clone this repository and its submodules into a folder of your choosing with `git clone --recurse-submodules https://github.com/SpencerWBarnes/PiMon.git`. Then navigate into the repository and run `sudo pipenv install`. This will install all necessary packages for the Pi.

*This app will need to run as **root** to get port 80 access!*

You may run into issues with `libsass` and `pipenv`. To fix this,
enter your development folder and run `sudo pipenv shell`. Then,
type `pipenv install libsass`. This bypasses `pipenv` but fixes the bug.


## Setup
The Pi must already be configured:
1) As a wireless access point. Requiring:
   * Wireless abilities, built in or as a dongle
   * Set up as a DNS server *
   * Set up as a DHCP server **
   * Set IP address of host device (Pi)
2) With Redis server
3) With SerialManager _[GitHub here](https://github.com/MSUSeconRobotics/SerialManager.git)_

<sub>
* So the Pi can tell connected devices the IP address of websites
<br>
** So the Pi can give connected devices an IP address
</sub>
<br><br>

In order to run services on bootup, a script must be added to `/etc/init.d/`
and the run `sudo update-rc.d <FileName> defaults`.
> RC scripts explained [here](https://docs.oracle.com/cd/E19683-01/806-4073/6jd67r96g/index.html)


## Development
PiMon is developed with the following:
* Python 3.7 + pipenv
* Bootstrap 4.3.1 + Bootswatch (Darkly)
* Flask
* Waitress

You may need C++ Build Tools to install all packages.

If you want an explanation or description of the code, reference the [Code Explained doc](/CodeExplained.md).

## Usage
PiMon runs on a Python Waitress server. The webpage's address is `192.168.1.1`

Run the app anywhere with:
```
sudo /etc/init.d/pimon start
```
and to stop the app:
```
sudo /etc/init.s/pimon stop
```

The app can also be run by executing the following command in the dev folder:
```
sudo pipenv run python app.py
```
or
```
sudo pipenv shell
python app.py
```

---
Please note that due to unanticipated circumstances _(global pandemic)_ we were not able to set up a second Pi with this configuration. 
We sincerely apologize if the above steps are incomplete, and **we would appreciate it if users would add to this repository**. 