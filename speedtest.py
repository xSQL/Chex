import timeit
from chex import Chex

def t_chex():
    c = Chex()
    for i in range(5):
        c.get_key_by_id(i+1)

def t2_chex():
    c = Chex()
    for i in range(5):
        k = c.get_key_by_id(i+1)
        if c.get_id_by_key(k) != i+1:
            print('Error!')
            break

print("ID to key: %s"%(timeit.timeit(t_chex, number=150000),)) 

print("ID to key & return: %s"%(timeit.timeit(t2_chex, number=150000),)) 
