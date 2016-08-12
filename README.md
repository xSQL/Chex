# Chex

How to use:

```python
from Chex import Chex

c = Chex()

print([67]) // print 'rrrrrrbt'
print(['rrrrrrbt']) // print 67
```

Also you may set custom hash length and set of chars

```python
from Chex import Chex

c = Chex()
c = Chex(4, 'abcdefg')

print(c['aaaa']) // print 1
```
