import logging
import string
from unidecode import unidecode

from ciphers.cipher import Cipher

class VigenereCipher(Cipher):
    def __init__(self, _source: str, __key: str) -> None:
        Cipher.__init__(self, _source)
        self.__key = __key

    def __formatting_text(self, text: str )-> str:
        '''
        Formats a capitalized text by removing accents, punctuation and spaces.
        >>> formatting_text("That's one small step for a man; one giant leap for mankind.")
        'THATSONESMALLSTEPFORAMANONEGIANTLEAPFORMANKIND'
        '''
        textFormat = ''
        charactersToEscape = string.punctuation + ' '

        for character in text:
            textFormat += '' if character in charactersToEscape else character

        return unidecode(textFormat).upper()
    
    def __define_corresponding_letter(self, letterMessage, letterKey, decrypted=False) -> str:
        '''
        Return the letter corresponding to the letter of the message and the letter of the key.
        >>> define_corresponding_letter('B', 'Z')
        'A'
        >>> define_corresponding_letter('A', 'Z', True)
        'B'
        '''
        if decrypted:
            if self._define_position_letter(letterMessage) - self._define_position_letter(letterKey) < 0:
                return chr(self._define_position_letter(letterMessage) - self._define_position_letter(letterKey) + 26 + 65)
            else:
                return chr(self._define_position_letter(letterMessage) - self._define_position_letter(letterKey) + 65)
        else:
            if self._define_position_letter(letterMessage) + self._define_position_letter(letterKey) > 25:
                return chr(self._define_position_letter(letterMessage) + self._define_position_letter(letterKey) - 26 + 65)
            else:
                return chr(self._define_position_letter(letterMessage) + self._define_position_letter(letterKey) + 65)
            
    
    def encrypt(self) -> str:
        '''
        Encrypts the message entered by the user using Vigenère cipher.
        >>> encrypt("J'adore écouter la radio toute la journée", "musique")
        "V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY"
        '''
        logging.info("vigenere_encryption")

        alphabet = string.ascii_uppercase
        encryptedArray = []

        for counter, letter in enumerate(self.__formatting_text(self._source)):
            if letter in alphabet:
                encryptedArray.append(
                    self.__define_corresponding_letter(
                        letter,
                        self.__formatting_text(self.__key)[counter % len(self.__formatting_text(self.__key))]
                    )
                )
                
        for counter, letter in enumerate(unidecode(self._source).upper()):
            if letter not in alphabet:
                encryptedArray.insert(counter, letter)

        return ''.join(encryptedArray)
    
    def decrypt(self) -> str:
        '''
        Encrypts the message entered by the user using Vigenère cipher.
        >>> decrypt("V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY", "musique")
        "J'ADORE ECOUTER LA RADIO TOUTE LA JOURNEE"
        '''
        logging.info("vigenere_decryption")

        alphabet = string.ascii_uppercase
        decryptedArray = []

        for counter, letter in enumerate(self.__formatting_text(self._source)):
            if letter in alphabet:
                decryptedArray.append(
                    self.__define_corresponding_letter(
                        letter,
                        self.__formatting_text(self.__key)[counter % len(self.__formatting_text(self.__key))], 
                        True
                    )
                )
                    
        for counter, letter in enumerate(unidecode(self._source).upper()):
            if letter not in alphabet:
                decryptedArray.insert(counter, letter)

        return ''.join(decryptedArray)