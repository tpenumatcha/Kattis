from math import factorial
combination = lambda x, y: factorial(x)/(factorial(y) * factorial(x - y))
characters = int(input())
relationships = 0
counter = 2
if characters > 1:
    while counter <= characters:
        relationships += combination(characters, counter)
        counter += 1
print(int(relationships))
