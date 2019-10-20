a = [x for x in [1,2,3] if True]
a = [x for x in ([1,2,3] if False else [3,2,1])]

#a = 'T' or ''
#print(a)
#a = False or None
#print(a)
#a = None or ''
#print(a)
#a = '' or None
#print(a)
#a = 'T' or 'F'
#print(a)
#a = False or 1==1
#print(a)

a = False or None or '' or 0 or [] or 3 or 'T'
print(a)

a = 1 if False else (2 if False else 3)
print(a)

a = (3)
print(type(a))

a = (3  ,  )
print(a)
print(type(a))

a = (x**2 for x in range(5))
print(a)
print(type(a))

a = set(x**2 for x in range(5))
print(a)
print(type(a))

a = {x**2 for x in range(5)}
print(a)
print(type(a))

a = {x**2: 1 for x in range(5)}
print(a)
print(type(a))

a = {}
print(a)
print(type(a))

a = {5}
print(a)
print(type(a))
