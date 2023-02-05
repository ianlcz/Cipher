import logging
import string
from unidecode import unidecode

from exceptions.configurationvalidation import ConfigurationValidationException

from ciphers.cipher import Cipher

class SubstitutionCipher(Cipher):
    def __init__(self, _source: str, __alphabet: str | None) -> None:
        Cipher.__init__(self, _source)
        self.__alphabet = __alphabet.upper().split(',')

    def __check(self) -> None:
        if len(self.__alphabet) != 26:
            raise ConfigurationValidationException('Alphabet must contain 26 letters')
        
        if ''.join(sorted(self.__alphabet)) != string.ascii_uppercase:
            raise ConfigurationValidationException('Alphabet must not have the same letter more than once')

    def encrypt(self) -> str:
        '''
        Encrypts the message entered by the user using the substitution method.
        >>> encrypt("Substitution", "a,z,e,r,t,y,u,i,o,p,q,s,d,f,g,h,j,k,l,m,w,x,c,v,b,n")
        'LWZLMOMWMOGF'
        '''
        logging.info("substitution_encryption")

        self.__check()

        encryptedMessage = ""

        for letter in unidecode(self._source).upper():
            search = string.ascii_uppercase.find(letter)

            encryptedMessage += letter if search < 0 else self.__alphabet[search] + ' ' if ''.join(sorted(self.__alphabet)) != string.ascii_uppercase else self.__alphabet[search]
            
        return encryptedMessage
    
    def decrypt(self) -> str:
        return super().decrypt()