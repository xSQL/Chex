from chex import Chex

def t_chex():
    c = Chex()
    for i in range(150000):
        c.get_key_by_id(i+1)

import timeit

print(timeit.timeit(t_chex, number=10)) # Or more.
