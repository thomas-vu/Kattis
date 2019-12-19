from collections import defaultdict

for _ in range(int(input())):
    people = {}
    classes = defaultdict(list)

    for _ in range(int(input())):
        line = input().split()
        people[line[0][:-1]] = line[1].split('-')

    for person in people:
        classNumber = ''
        for distinction in reversed(people[person]):
            if   distinction == 'upper':  classNumber += '1'
            elif distinction == 'middle': classNumber += '2'
            elif distinction == 'lower':  classNumber += '3'
        classNumber += '2' * (10-len(classNumber))
        classes[classNumber].append(person)

    for key in sorted(classes.keys()):
        for person in sorted(classes[key]):
            print(person)

    print('=' * 30)
