import logging
import string

from unidecode import unidecode

class CaesarConverter:
    def __init__(self, source: str, offset: int) -> None:
        self.source = source
        self.offset = offset

    def encrypt(self) -> str:
        '''
        Encrypts the message entered by the user using Caesar cipher.
        >>> caesar_encryption("Caesar", 2)
        'ECGUCT'
        '''
        logging.info("caesar_encryption")

        message = ""

        for letter in unidecode(self.source).upper():

            if letter not in string.digits and letter not in string.punctuation and letter not in string.whitespace:
                newLetter = ord(letter) - 65 + self.offset

                if newLetter > 25:
                    newLetter -= 26

                message += chr(newLetter + 65)
            else:
                message += letter
                
        return 'message:' + message