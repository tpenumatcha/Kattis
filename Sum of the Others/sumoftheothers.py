import sys
for line in sys.stdin:
    data = line.split()
    numbers = []
    for value in data:
        numbers.append(int(value))
    for i in range(len(numbers)):
        if sum(numbers) - numbers[i] == numbers[i]:
            print(numbers[i])
            break
