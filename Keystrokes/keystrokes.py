strokes = list(input())
output = []
i = 0
cursor = i
while i < len(strokes):
    if strokes[i] not in ["L", "R", "B"]:
        output.insert(cursor, strokes[i])
        cursor += 1
    elif strokes[i] == "L":
        cursor -= 1
    elif strokes[i] == "R":
        if cursor < i:
            cursor += 1
    elif strokes[i] == "B":
        del output[cursor - 1]
        cursor -= 1
    i += 1
print("".join(output))
