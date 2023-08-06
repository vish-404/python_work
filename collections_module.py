from abc import abstractproperty
import collections
# goto docs

player = collections.namedtuple("player", ["name" , "age", "team"] )
p1 = player("Prakhar", 18, "IITISM")
print(p1.name, p1.age, p1.team , "\n\n")

d1  = collections.OrderedDict()
d1["first: "] = 30
d1["second: "] = 40
d1["third: "] = 45
d1["fourth: "] = 55
for k , v in d1.items():
    print(k, v)

q = collections.deque([20, 30, 45, 86])
print(q.pop(), q.popleft() , "\n", q)
q.append(10)
print(q)
q.appendleft(154)
print(q)

x = [8, 1, 5, 2, 1, 7, 5, 0, 3, 4, 6, 3, 3, 9, 3, 5]
print(list(collections.Counter(x).items()), "\n")
print(list(collections.Counter(x).keys()), "\n")
print(list(collections.Counter(x).values()), "\n")