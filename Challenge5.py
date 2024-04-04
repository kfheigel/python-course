class DNABase:
    
    nucleotides = {'adenine', 'cytosine', 'guanine', 'thymine'}
    
    def __init__(self, nucleotide) -> None:
        self.base = nucleotide
    
    def __repr__(self) -> str:
        return (f"{type(self).__name__}(nucelotide='{self._base}')")
    
    def set_nucleotide(self, base):
        valid_base = self._validate_and_standardize(base)
        if valid_base:
            self._base = valid_base
        else:
            raise ValueError(f"{base} is not a recognized DNA nucleotide")
        
    @staticmethod
    def _validate_and_standardize(base):
        allowed = [('a', 'adenine'), ('c', 'cytosine'), ('g', 'guanine'), ('t', 'thymine')]
        
        for b in allowed:
            if base.lower().strip() in b:
                return b[1]
            
        return False
        
    def get_nucleotide(self):
        return self._base
    
    base = property(fget=get_nucleotide, fset=set_nucleotide)
 

d = DNABase('thyMiNE')

print(d.get_nucleotide())
 