def solution(stores, houses):
    A = []
    for h in houses:
        smallestdist = 1000000000
        closeststore = 1000000000
        for s in stores:
            dist = abs(h-s)
            if dist < smallestdist:
                smallestdist = dist
                closeststore = s
            elif dist == smallestdist and s < closeststore:
                closeststore = s
        A.append(closeststore)
    return A

stores = [int(x) for x in input().split()]
houses = [int(x) for x in input().split()]
print(solution(stores, houses))
