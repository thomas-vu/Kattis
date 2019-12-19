# assuming mappings are unique
try:

    while True:
        domain = set([x for x in input().split()][1:])
        codomain = set([x for x in input().split()][1:])
        d = set()
        cd = set()
        injective = True
    
        for _ in range(int(input())):
            a, _, b = [x for x in input().split()]
    
            if a in d:
                print('not a function')
                break
            
            if b in cd:
                injective = False
                
            d.add(a)
            cd.add(b)

        else:
            if not injective and cd != codomain:
                print('neither injective nor surjective')
            elif injective and cd != codomain:
                print('injective')
            elif not injective and cd == codomain:
                print('surjective')
            elif injective and cd == codomain:
                print('bijective')

except EOFError as e:
    pass
