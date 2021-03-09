import sys
definitions = {}
for line in sys.stdin:
    command = line.split()
    if command[0] == "def":
        definitions[command[1]] = command[2]
    elif command[0] == "calc":
        operation = ""
        unknown = False
        for i in range(1, len(command) - 1):
            if command[i] in ['+', '-']:
                operation += command[i]
            elif command[i] in definitions:
                operation += definitions[command[i]]
            else:
                unknown = True
        if unknown:
            print(" ".join(command[1:]) + " unknown")
        else:
            temp = eval(operation)
            defkeys = list(definitions.keys())
            defvalues = list(definitions.values())
            if str(temp) in defvalues:
                position = defvalues.index(str(temp))
                print(" ".join(command[1:]) + " " + defkeys[position])
            else:
                print(" ".join(command[1:]) + " unknown")
    elif command[0] == "clear":
        definitions.clear()
