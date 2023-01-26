import logging
import platform

import click

from exceptions.configurationvalidation import ConfigurationValidationException

from ciphers.caesar import CaesarCipher

@click.group()
@click.pass_context
def cli(ctx):
    '''
    A CLI tool to encrypt or decrypt different messages using several encryption methods.
    '''
    pass

@cli.command()
@click.option('-m', '--message', type=str, prompt=True, help='Message to be encrypted')
@click.option('-s', '--shift', type=int, default=2, show_default=True, help='Character shift' )
@click.option('-d', '--decrypted', is_flag=True, default=False, help='Allows to decrypt a message')
@click.pass_context
def caesar(ctx, message, shift, decrypted):
    '''
    Encrypt the message entered by the user using Caesar cipher
    '''
    if message:
        caesar = CaesarCipher(message, shift)

        logging.info(caesar.decrypt() if decrypted else caesar.encrypt())
    else:
        raise AttributeError('Message to be encrypted not found')

@click.command()
def main() -> None:
    pass

def configure_logging() -> None:
    logging.basicConfig(level='INFO')

if __name__ == '__main__':

    try:
        configure_logging()

        logging.info('python: ' + platform.python_version())
        logging.info('system: ' + platform.system())
        logging.info('machine: ' + platform.machine())

        cli()

    except ConfigurationValidationException as e:
        logging.error("CONFIGURATIONS ERROR")
        logging.error(e.message)
