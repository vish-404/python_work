import itertools
import time
t1 = time.time()

l1 = ['1','2','3']
l2 = ['5','4','3']
print(list(itertools.product(l1, l2)), "\n")
print(list(itertools.product(l1,repeat = 2)), "\n")
print(list(itertools.permutations(l1)), "\n")
print(list(itertools.permutations(l1, 2)), "\n")
print(list(itertools.combinations(l1, 3)), "\n") # in combinations the integer must be given
print(list(itertools.combinations(l1, 2)), "\n")
print(list(itertools.combinations_with_replacement(l1, 2)))

t2 = time.time()
print(t2 - t2)