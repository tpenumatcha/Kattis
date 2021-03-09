import sys
definitions = {}
for line in sys.stdin:
    temp = line.split()
    if temp[0] == "define":
        definitions[temp[2]] = int(temp[1])
    if temp[0] == "eval":
        if temp[2] == "=":
            temp[2] = "=="
        if temp[1] in definitions.keys() and temp[3] in definitions.keys():
            print(str(eval(str(definitions[temp[1]]) + " " + temp[2] + " " + str(definitions[temp[3]]))).lower())
        else:
            print("undefined")
