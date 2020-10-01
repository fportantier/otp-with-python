Really simple One Time Password example with Python
===================================================

Command line application that supports 3 commands:

1. generate: To generate an OTP secret on /tmp/otp-with-python.txt
2. show: To show a QR code on the terminal
3. validate: To check if your code it's correct


Dependencies
------------

Only need 3 packages: click, pyotp and qrcode.

With APT on Debian, Ubuntu, etc.
................................

::

    $ sudo apt-get install python3-click, python3-pyotp, python3-qrcode


With pip
........

::

    $ pip3 install click pyotp qrcode


Installation
------------

Clone the repo and execute the tool with:

::

    $ git clone https://github.com/fportantier/otp-with-python
    cd opt-with-python
    ./otp-with-python.py


