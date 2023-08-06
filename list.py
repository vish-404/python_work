import copy   # to copy the list  ........ 
string = "abcdeaAE"
lst = [1, 4, 5, 3, -3, -9, 0]
strr = ['aman', 'hello', 'hi', 'zayn', 'karan', 'ice']
l = list(string)
print(l)

print(l.index('b'))

char = copy.copy(lst)
char.remove(0)
print(lst)
print(char)

l.append('f')
print(l)
l.extend(['t', 'y'])
print(l)
print(l.count('a'))

l.remove('a')
print(l)

l.sort()
print(l)

l.insert(3, 'B')
print(l)

l.sort(key= str.lower)
print(l)
l.sort()
print(l)

strr.sort()
print(strr)
strr.sort(reverse= True)
print(strr)
strr.reverse()
print(strr)

lst.sort()
print(lst)
lst.sort(reverse= True)
print(lst)

print(*lst, sep= " ")  # to get rid of square bracket of integer list
print(' '.join(strr))  # to get rid of square bracket of character or word  list

new = iter(string)  #to use iter function
print(next(new))
print(next(new))
print(next(new))
print(next(new))
print(next(new))

new = iter(lst)  # can be used in all iterable obj.
print(next(new))
print(next(new))