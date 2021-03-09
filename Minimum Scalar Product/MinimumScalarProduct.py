cases = int(input())
answers = []
for i in range(cases):
    dp = 0
    length = int(input())
    vector1 = input().split()
    vector2 = input().split()
    v1 = []
    v2 = []
    for s in range(length):
        v1.append(int(vector1[s]))
        v2.append(int(vector2[s]))
    while not (len(v1) == 0 and len(v2) == 0):
        dp += max(v1) * min(v2)
        v1.remove(max(v1))
        v2.remove(min(v2))
    answers.append(dp)
for m in range(len(answers)):
    print(f"Case #{m + 1}: {answers[m]}")
