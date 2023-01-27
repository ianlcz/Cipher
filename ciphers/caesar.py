import logging
import string
from unidecode import unidecode

from ciphers.cipher import Cipher

class CaesarCipher(Cipher):
    def __init__(self, _source: str, __offset: int) -> None:
        Cipher.__init__(self, _source)
        self.__offset = __offset

    def encrypt(self) -> str:
        '''
        Encrypts the message entered by the user using Caesar cipher.
        >>> encrypt("Caesar", 2)
        'ECGUCT'
        '''
        logging.info("caesar_encryption")

        encryptedMessage = ""

        for letter in unidecode(self._source).upper():

            if letter not in string.digits and letter not in string.punctuation and letter not in string.whitespace:
                newLetter = self._define_position_letter(letter) + self.__offset

                if newLetter > 25:
                    newLetter -= 26

                encryptedMessage += chr(newLetter + 65)
            else:
                encryptedMessage += letter
                
        return encryptedMessage
    
    def decrypt(self) -> str:
        '''
        Decrypts the encrypted message entered by the user using Caesar cipher.
        >>> decrypt("ecguct", 2)
        'CAESAR'
        '''
        logging.info("caesar_decryption")

        decryptedMessage = ""

        for letter in unidecode(self._source).upper():
            if letter not in string.digits and letter not in string.punctuation and letter not in string.whitespace:
                newLetter = self._define_position_letter(letter) - self.__offset

                if newLetter < 0:
                    newLetter += 26
                    
                decryptedMessage += chr(newLetter + 65)
            else:
                decryptedMessage += letter

        return decryptedMessage