

def interpret(code):
    output = ""
    stack = []
    x=0
    y=0

    while(code[x][y] != '@'):
        match(code[x][y]):
            case "":
                break
            case "+":
                break
            case "-":
                break
            case "*":
                break
            case "/":
                break
            case "%":
                break
            case "!":
                break
            case "`":
                break
            case ">":
                break
            case "<":
                break
            case "^":
                break
            case "v":
                break
            case "?":
                break
            case "_":
                break
            case "|":
                break
            case "\"":
                break
            case ":":
                break
            case "\\":
                break
            case "$":
                break
            case ".":
                break
            case ",":
                break
            case "#":
                break
            case "p":
                break
            case "g":
                break

    # TODO: Interpret the code!
    return output