import random
import math


class OverRangeException(Exception):
    """..."""
    
    def __init__(self, message):
        """..."""        
        self.message = message


class Chex:
    """..."""
    size = 8
    phrase = 'rabszcowejvglutyhkqmnfpixd'
    str_values = dict()
    int_values = dict()
    
    def __init__(self, size=None, phrase=None):
        """..."""        
        if size:
            self.size = size
        if phrase:
            self.phrase = phrase

    def __getitem__(self, key):
        """..."""
        if type(key)==int:
            self.key = key-1            
            if key>len(self.phrase)**self.size:
                raise OverRangeException("Key %s is very big."%(key,))
            elif key<1:
                raise OverRangeException("Key %s is very small."%(key,))                
            return str(self)
        else:
            self.key = key
            return int(self)
    
    def __str__(self):
        """..."""        
        if not self.str_values.get(self.key, False):
            rank=0
            digit = self.key
            size = self.size
            length = len(self.phrase)
            values = list()
            results = [self.phrase[0] for i in range(size)]            
            while digit/length>1:
                i = digit%length
                results[size-1] = self.phrase[i]
                size -= 1                
                rank+=1
                digit=digit//length
            results[size-1] = self.phrase[digit]
            self.str_values[self.key] = ''.join(results)
        return self.str_values[self.key]

    
    def __int__(self):
        """..."""        
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
               
            self.int_values[self.key] = total+1
        return self.int_values[self.key]

