import random
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

    def __init__(self, size=None, phrase=None):
        self.str_values = dict()
        self.int_values = dict()
        """Initialize code length and chars set"""        
        self.size = size if size else 8
        self.phrase = phrase if phrase else \
        'rabszcowejvglutyhkqmnfpixd'

    def __getitem__(self, key):
        """Return code or decimal digit."""
        if isinstance(key, int):
            self.key = key            
            if key>len(self.phrase)**self.size:
                raise OverRangeException("Key %s is very big."%(key,))
            elif key<1:
                raise OverRangeException("Key %s is very small."%(key,))                
            res = str(self)
            self.int_values[res] = key
            return res
        else:
            self.key = key
            res = int(self)
            self.str_values[res] = key
            return res            
    
    def __str__(self):
        """Function to encode."""        
        if not self.str_values.get(self.key, False):
            rank=0
            digit = self.key
            size = self.size-1
            length = len(self.phrase)
            results = [self.phrase[0] for i in range(size+1)]            
            while digit/length>=1:
                i = digit%length
                results[size] = self.phrase[i]
                size -= 1                
                rank+=1
                digit=digit//length
            results[size] = self.phrase[digit]
            self.str_values[self.key] = ''.join(results)
        return self.str_values[self.key]

    
    def __int__(self):
        """Function to decode."""        
        size =len(self.phrase)
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
                if j==0:
                    total = positions[i]
                else:
                    total += (size**j)*positions[i]
       
                j+=1
               
            self.int_values[self.key] = total
        return self.int_values[self.key]
