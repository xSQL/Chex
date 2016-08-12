import math


class OverRangeException(Exception):
    """Exception class to Chex"""
    
    def __init__(self, message):
        """You may add custom meesage, when throw this exception"""        
        self.message = message


class Chex:
    """Encode && decode decimal digits from custom set of chars
    
    use like:
        c = Chex()
        c[key]

   'key' may be string or int:
    if key is integer then hi will be encoded to string and returned
    if key is string then hi will be decoded to int and returned    
    
    """  

    def __init__(self, size=8, phrase='uabszcowejvglrtyhkqmnfpixd'):
        """Initialize code length and chars set"""        
        self.str_values = dict()
        self.int_values = dict()
        self.size = size
        self.phrase = phrase
        self.phrase_len = len(self.phrase)

    def __getitem__(self, key):
        """Return code or decimal digit."""
        self.key = key
        if isinstance(key, int):
            if key>self.phrase_len**self.size:
                raise OverRangeException("Key %s is very big."%(key,))
            elif key<1:
                raise OverRangeException("Key %s is very small."%(key,))                
            res = str(self)
            self.int_values[res] = key
            return res
        else:
            res = int(self)
            self.str_values[res] = key
            return res            
    
    def __str__(self):
        """Function to encode."""        
        if not self.str_values.get(self.key, False):
            digit = self.key
            size = self.size-1
            length = self.phrase_len
            results = [self.phrase[0]]*(size+1)            
            while True:
                digit, i = divmod(digit, length)
                results[size] = self.phrase[i]
                size -= 1                
                if digit==0:
                    break
            self.str_values[self.key] = ''.join(results)
        return self.str_values[self.key]
    
    def __int__(self):
        """Function to decode."""        
        size = self.phrase_len
        if not self.int_values.get(self.key, False):
            positions = dict()
            length = len(self.key)-1
            j = 0
            total = 0
            while length>=0:
                i=self.key[length]
                length-=1
                if not positions.get(i, False):
                    positions[i] = self.phrase.index(i)
                total += (size**j)*positions[i]
                j+=1
            self.int_values[self.key] = total
        return self.int_values[self.key]

