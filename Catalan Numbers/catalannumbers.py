from math import factorial


def catalan(x, y):
    x, y = float(x), float(y)
    return factorial(x) // (factorial(y + 1) * factorial(x - y))


cases = int(input())
answers = []
for i in range(cases):
    num = float(input())
    cat = catalan(num * 2, num)
    answers.append(cat)

for each in answers:
    print(each)
