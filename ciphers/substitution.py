import logging
import string

from exceptions.configurationvalidation import ConfigurationValidationException

from ciphers.cipher import Cipher

class SubstitutionCipher(Cipher):
    def __init__(self, _source: str, __alphabet: str) -> None:
        Cipher.__init__(self, _source)
        self.__alphabet = __alphabet.upper().split(',')

    def _check(self) -> None:
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

        self._check()

        encryptedMessage = ""

        for letter in self._source.upper():
            search = string.ascii_uppercase.find(letter)

            encryptedMessage += letter if search < 0 else self.__alphabet[search] + ' ' if ''.join(sorted(self.__alphabet)) != string.ascii_uppercase else self.__alphabet[search]
            
        return encryptedMessage
    
    def decrypt(self) -> str:
        '''
        Decrypts the message entered by the user using the substitution method.
        >>> decrypt("LWZLMOMWMOGF",  "a,z,e,r,t,y,u,i,o,p,q,s,d,f,g,h,j,k,l,m,w,x,c,v,b,n")
        'SUBSTITUTION'
        '''
        logging.info('substitution_decryption')

        self._check()

        decryptedMessage = ""
        
        for letter in self._source.upper():
                search = ''.join(self.__alphabet).find(letter)

                decryptedMessage += letter if search < 0 else string.ascii_uppercase[search]
                    
        return decryptedMessage