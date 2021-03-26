cases = int(input())
answers = []
for i in range(cases):
    candidates = int(input())
    results = []
    for j in range(candidates):
        results.append(int(input()))
    total = sum(results)
    highest = max(results)
    if results.count(highest) > 1:
        answers.append("no winner")
    elif highest / total > 0.5:
        answers.append(f"majority winner {results.index(highest) + 1}")
    elif highest / total <= 0.5:
        answers.append(f"minority winner {results.index(highest) + 1}")
for each in answers:
    print(each)
