import logging
import platform

import click

from exceptions.configurationvalidation import ConfigurationValidationException

from converters.caesar import CaesarConverter

@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.command()
@click.option('--message', help='Message to be encrypted')
@click.option('--offset', default=2, help='Character shift' )
@click.pass_context
def caesar(ctx, message, offset):
    '''
    Encrypt the message entered by the user using Caesar cipher
    '''
    if message:
        caesar = CaesarConverter(message, offset)
        logging.info(caesar.encrypt())
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
