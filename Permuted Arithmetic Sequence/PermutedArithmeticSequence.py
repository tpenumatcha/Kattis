cases = int(input())
ans = []


def sortThis(arr):
    newarr = []
    for each in arr:
        newarr.append(int(each))
    finalarr = sorted(newarr)
    return finalarr


def checkdiff(arr):
    length = len(arr) - 1
    diff = int(arr[1]) - int(arr[0])
    for j in range(len(arr)):
        if not(j == length):
            if not (int(arr[j + 1]) - int(arr[j]) == diff):
                return False
    return True


for i in range(cases):
    case = input().split()
    case.remove(case[0])
    if checkdiff(case):
        ans.append("arithmetic")
    else:
        x = sortThis(case)
        if checkdiff(x):
            ans.append("permuted arithmetic")
        else:
            ans.append("non-arithmetic")
for each in ans:
    print(each)
