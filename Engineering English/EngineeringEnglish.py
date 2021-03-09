import sys

sentence = set()
for line in sys.stdin:
    output = []
    for word in line.split():
        if word.lower() in sentence:
            output.append(".")
        else:
            output.append(word)
            sentence.add(word.lower())
    print(" ".join(output))
