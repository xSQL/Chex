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
        if not isinstance(size, int):
            raise TypeError('Size must be set as integer')
        if size<1:
            raise ValueError('Size must be grate than 0')
        if not isinstance(phrase, str):
            raise TypeError('Alphabet phrase must be set as string')
        if len(phrase)!=len(set(phrase)):
            raise ValueError('Alphabet contain duplicates')
        
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
                raise KeyError("Key %s is very big."%(key,))
            elif key<1:
                raise KeyError("Key %s is very small."%(key,))                
            res = str(self)
            self.int_values[res] = key
            return res
        elif isinstance(key, str):
            res = int(self)
            self.str_values[res] = key
            return res
        else:
            raise KeyError
    
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

