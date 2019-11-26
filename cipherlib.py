import string
from unidecode import unidecode


def define_position_letter(letter):
    """
    Return the alphabetical position of the letter set as parameter of the function.
    >>> define_position_letter('A')
    0
    >>> define_position_letter('Z')
    25
    """
    return ord(letter) - 65


def caesar_encryption(message, offset, decode=False):
    '''
    Encrypts or decrypts the message entered by the user using Caesar cipher.
    >>> caesar_encryption("Caesar", 3)
    'FDHVDU'
    >>> caesar_encryption("FDHVDU", 3, True)
    'CAESAR'
    '''
    CaesarsCodeMessage = ""
    for letter in unidecode(message).upper():
        if letter not in string.digits and letter not in string.punctuation and letter not in string.whitespace:
            if decode:
                newLetter = define_position_letter(letter) - offset
                if newLetter < 0:
                    newLetter += 26
            else:
                newLetter = define_position_letter(letter) + offset
                if newLetter > 25:
                    newLetter -= 26
            CaesarsCodeMessage += chr(newLetter + 65)
        else:
            CaesarsCodeMessage += letter
    return CaesarsCodeMessage


def substitution_encryption(message, key, decode=False):
    '''
    Encrypts or decrypts the message entered by the user using the substitution method.
    >>> substitution_encryption("Substitution", ['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N'])
    'LWZLMOMWMOGF'
    >>> substitution_encryption("LWZLMOMWMOGF",  "AZERTYUIOPQSDFGHJKLMWXCVBN", True)
    'SUBSTITUTION'
    '''
    alphabet = string.ascii_uppercase
    substitutionEncryptionMessage = ""
    for letter in unidecode(message).upper():
        search = key.find(letter) if decode else alphabet.find(letter)
        substitutionEncryptionMessage += letter if search < 0 else alphabet[
            search] if decode else key[search]
    return substitutionEncryptionMessage


def vigenere_encryption(message, key, decode=False):
    """
    Encrypts the message entered by the user using Vigenère cipher.
    >>> vigenere_encryption("J'adore écouter la radio toute la journée", "musique")
    "V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY"
    >>> vigenere_encryption("V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY", "musique", True)
    "J'ADORE ECOUTER LA RADIO TOUTE LA JOURNEE"
    """

    def define_corresponding_letter(letterMessage, letterKey, decode=False):
        """
        Return the letter corresponding to the letter of the message and the letter of the key.
        >>> define_corresponding_letter('B', 'Z')
        'A'
        >>> define_corresponding_letter('A', 'Z', True)
        'B'
        """
        if decode:
            if define_position_letter(letterMessage) - \
                    define_position_letter(letterKey) < 0:
                return chr(define_position_letter(letterMessage) -
                           define_position_letter(letterKey) + 26 + 65)
            else:
                return chr(define_position_letter(letterMessage) -
                           define_position_letter(letterKey) + 65)
        else:
            if define_position_letter(letterMessage) + \
                    define_position_letter(letterKey) > 25:
                return chr(define_position_letter(letterMessage) +
                           define_position_letter(letterKey) - 26 + 65)
            else:
                return chr(define_position_letter(letterMessage) +
                           define_position_letter(letterKey) + 65)

    alphabet = string.ascii_uppercase
    VigeneresCodeMessage = []
    for counter, letter in enumerate(unidecode(message).replace(
            "'",
            '').replace(
            ' ',
            '').replace(
                ',',
                '').replace(
                    '.',
            '').replace('\t', '').upper()):
        if letter in alphabet:
            if decode:
                VigeneresCodeMessage.append(
                    define_corresponding_letter(
                        letter,
                        unidecode(key).upper()[
                            counter % len(
                                unidecode(key).upper())], True))
            else:
                VigeneresCodeMessage.append(
                    define_corresponding_letter(
                        letter,
                        unidecode(key).upper()[
                            counter % len(
                                unidecode(key).upper())]))
    for counter, letter in enumerate(unidecode(message).upper()):
        if letter not in alphabet:
            VigeneresCodeMessage.insert(counter, letter)
    return ''.join(VigeneresCodeMessage)
