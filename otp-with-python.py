#!/usr/bin/env python3

import logging
from pathlib import Path

import click
import pyotp
import qrcode

logging.basicConfig()
secret_file = Path('/tmp/otp-with-python.txt')


@click.group()
def cli():
    pass


@cli.command()
def generate():
    with secret_file.open('w') as outfile:
        outfile.write(pyotp.random_base32())


@cli.command()
def show():

    if not secret_file.is_file():
        logging.error('Use the "generate" command first!')
        return False

    with secret_file.open('r') as infile:
        secret = infile.read()

    uri = pyotp.totp.TOTP(secret).provisioning_uri("OTP-With-Python")

    qr = qrcode.QRCode()
    qr.add_data(uri)
    qr.print_ascii()


@cli.command()
@click.argument('value')
def validate(value):

    if not secret_file.is_file():
        logging.error('Use the "generate" command first!')
        return False

    with secret_file.open('r') as infile:
        secret = infile.read()

    totp = pyotp.totp.TOTP(secret)

    if totp.verify(value):
        print('OK - VALID CODE!')
    else:
        print('ERROR - INVALID CODE!')


if __name__ == '__main__':
    cli()
