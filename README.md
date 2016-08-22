# Chex

How to use:

```python
from Chex import Chex

c = Chex()

print(c.get_key_by_id(67)) // print 'rrrrrrbt'
print(c.get_id_by_key('rrrrrrbt')) // print 67
```

Also you may set custom hash length and set of chars

```python
from Chex import Chex

c = Chex()
c = Chex(4, 'abcdefg')

print(c.get_id_by_key('aaab')) // print 1
```
