cases = int(input())
answers = []
for i in range(cases):
    sounds = []
    recording = input().split()
    while True:
        animal = input().split()
        if animal == ["what", "does", "the", "fox", "say?"]:
            break
        sounds.append(animal[2])
    j = 0
    while j < len(recording):
        if recording[j] in sounds:
            del recording[j]
            j = 0
        else:
            j += 1
    answers.append(' '.join(recording))
for each in answers:
    print(each)
