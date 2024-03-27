import random
import string

class Password:
    """A password of customize strength and length

    Returns:
        string: generated password based on strength ('low', 'mid', 'high')
    """
    DEFAULT_LENGTHS = {
        "low": 8,
        "mid": 12,
        "high": 16
    }
    
    password = ''
       
    def __init__(self, strength="mid", length=None):
        """Constructor method"""
        self.strength = strength
        self.password = self._generate(length)
    
    def _generate(self, length):
        match self.strength:
            case 'low':
                signs = string.ascii_letters
                length = length if length is not None else self.DEFAULT_LENGTHS[self.strength]
                return ''.join(random.choice(signs) for _ in range(length))
            
            case 'mid':
                signs = string.ascii_letters + string.digits
                length = length if length is not None else self.DEFAULT_LENGTHS[self.strength]
                return ''.join(random.choice(signs) for _ in range(length))
            
            case 'high':
                signs = string.ascii_letters + string.digits + string.punctuation
                length = length if length is not None else self.DEFAULT_LENGTHS[self.strength]
                return ''.join(random.choice(signs) for _ in range(length))
            
            case _: return ''

p1 = Password(strength = 'mid')
print(p1.password)
