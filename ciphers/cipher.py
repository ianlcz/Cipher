from abc import ABC, abstractmethod

class Cipher(ABC):
    '''    
    Attributes:
    -----------
     - source        Source message to be encrypted or decrypted
    '''

    def __init__(self, source: str) -> None:
        self._source = source

    def _define_position_letter(self, letter) -> int:
        '''
        Return the alphabetical position of the letter set as parameter of the function.
        >>> _define_position_letter('A')
        0
        >>> _define_position_letter('Z')
        25
        '''
        return ord(letter) - 65
    
    @abstractmethod
    def encrypt(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def decrypt(self) -> str:
        raise NotImplementedError