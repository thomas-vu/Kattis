n, dm = [int(x) for x in input().split()]
di = [int(x) for x in input().split()]
ind = -1
for i, x in enumerate(di):
    if x <= dm:
        ind = i
        break
if ind != -1:
    print("It hadn't snowed this early in", ind, "years!")
else:
    print("It had never snowed this early!")
