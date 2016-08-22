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
        
        self.size = size
        self.phrase = phrase
        self.phrase_len = len(self.phrase)
    
    def get_key_by_id(self, id):
        """Function to encode."""
        if not isinstance(id, int):
            raise TypeError('ID mustr be integer')        
        if id>self.phrase_len**self.size:
            raise ValueError("Key %s is very big."%(id,))
        elif id<1:
            raise ValueError("Key %s is very small."%(id))          
        digit = id
        size = self.size-1
        length = self.phrase_len
        results = [self.phrase[0]]*(size+1)            
        while True:
            digit, i = divmod(digit, length)
            results[size] = self.phrase[i]
            size -= 1                
            if digit==0:
                break
        return ''.join(results)
    
    def get_id_by_key(self, key):
        """Function to decode."""
        if not isinstance(key, str):
            raise TypeError('Key must be a string')                
        size = self.phrase_len
        positions = dict()
        length = len(key)-1
        j = 0
        total = 0
        while length>=0:
            i=key[length]
            length-=1
            if not positions.get(i, False):
                positions[i] = self.phrase.index(i)
            total += (size**j)*positions[i]
            j+=1
        return total
 
