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
        return super().encrypt()
    
    def decrypt(self) -> str:
        '''
        Decrypts the message entered by the user using the substitution method.
        >>> decrypt("-.-. --- -.. .  -- --- .-. ... .")
        'CODE MORSE'
        '''
        morseEquivalent = dict({'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '': ' '})

        decryptedMessage = ""

        for letter in self._source.split(' '):
            decryptedMessage += morseEquivalent[letter]
        
        return decryptedMessage