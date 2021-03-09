from collections import OrderedDict
cases = int(input())
name = []
course = []
scheduling = {}
for i in range(cases):
    entry = input().split()
    name.append(entry[0] + entry[1])
    course.append(entry[2])
for j in range(len(course)):
    if course[j] not in scheduling:
        scheduling[course[j]] = name[j].split()
    elif name[j] not in scheduling[course[j]]:
        scheduling[course[j]].append(name[j])
scheduling = OrderedDict(sorted(scheduling.items()))
for each in scheduling:
    print(f"{each} {len(scheduling[each])}")
