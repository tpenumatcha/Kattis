cases = int(input())
answers = []
for i in range(cases):
    statement = input()
    if "simon says " in statement:
        answers.append(statement[11:])
    else:
        answers.append("")
for each in answers:
    print(each)
