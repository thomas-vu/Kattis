def HasPairWithSumSorted(arr, target):
    low = 0
    hi = len(arr)-1
    while low != hi:
        s = arr[low] + arr[hi]
        if s == target:
            return (arr[low], arr[hi])
        elif s < target:
            low += 1
        elif s > target:
            hi -= 1
    return False

def HasPairWithSum(arr, target):
    comp = set()
    for x in arr:
        if x in comp:
            return (target-x, x)
        comp.add(target-x)
    return False

target = int(input())
arr = [int(x) for x in input().split()]
print(HasPairWithSum(arr, target))
