import logging
import platform

import click

from exceptions.configurationvalidation import ConfigurationValidationException

from ciphers.caesar import CaesarCipher
from ciphers.vigenere import VigenereCipher
from ciphers.substitution import SubstitutionCipher

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
def caesar(ctx, message: str, shift: int, decrypted: bool):
    '''
    Encrypt or decrypt the message entered by the user using Caesar cipher
    '''
    caesar = CaesarCipher(message, shift)
    print(caesar.decrypt() if decrypted else caesar.encrypt())

    
@cli.command()
@click.option('-m', '--message', type=str, prompt=True, help='Message to be encrypted')
@click.option('-k', '--key', type=str, prompt=True, help='Cipher key' )
@click.option('-d', '--decrypted', is_flag=True, default=False, help='Allows to decrypt a message')
@click.pass_context
def vigenere(ctx, message: str, key: str, decrypted: bool):
    '''
    Encrypt or decrypt the message entered by the user using Vigenère cipher
    '''
    vigenere = VigenereCipher(message, key)
    print(vigenere.decrypt() if decrypted else vigenere.encrypt())

@cli.command()
@click.option('-m', '--message', type=str, prompt=True, help='Message to be encrypted')
@click.option('-a', '--alphabet', type=str, prompt=True, help='Substitution alphabet' )
@click.pass_context
def substitution(ctx, message: str, alphabet: str):
    '''
    Encrypt the message entrered by the user using Substitution cipher
    '''
    substitution = SubstitutionCipher(message, alphabet)
    print(substitution.encrypt())

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
        logging.error(e.message)
