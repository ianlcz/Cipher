import logging
import string

from exceptions.configurationvalidation import ConfigurationValidationException

from ciphers.substitution import SubstitutionCipher

class MorseCode(SubstitutionCipher):
    def __init__(self, _source: str, __alphabet: str = ".-,-...,-.-.,-..,.,..-.,--.,....,..,.---,-.-,.-..,--,-.,---,.--.,--.-,.-.,...,-,..-,...-,.--,-..-,-.--,--..") -> None:
        super().__init__(_source, __alphabet)
        self.__alphabet = __alphabet

    def _check(self) -> None:
        if len(self.__alphabet) < 26:
            raise ConfigurationValidationException('Alphabet must contain at least 26 letters')
        
    def encrypt(self) -> str:
        '''
        Encrypts the message entered by the user using the substitution method.
        >>> encrypt("Code Morse")
        '-.-. --- -.. .  -- --- .-. ... .'
        '''
        logging.info('morse_encryption')

        self._check()

        encryptedMessage = ""

        for letter in self._source.upper():
            search = string.ascii_uppercase.find(letter)

            encryptedMessage += letter if search < 0 else self.__alphabet[search] + ' ' if ''.join(sorted(self.__alphabet)) != string.ascii_uppercase else self.__alphabet[search]
            
        return encryptedMessage
    
    def decrypt(self) -> str:
        '''
        Decrypts the message entered by the user using the substitution method.
        >>> decrypt("-.-. --- -.. .  -- --- .-. ... .")
        'CODE MORSE'
        '''
        logging.info('morse_decryption')

        morseEquivalent = dict({'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '': ' '})

        decryptedMessage = ""

        for letter in self._source.split(' '):
            decryptedMessage += morseEquivalent[letter]
        
        return decryptedMessage