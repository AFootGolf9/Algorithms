

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
                stack.append(int(stack.pop()) + int(stack.pop()))
                break
            case "-":
                stack.append(int(stack.pop()) - int(stack.pop()))
                break
            case "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
                break
            case "/":
                stack.append(int(stack.pop()) / int(stack.pop()))
                break
            case "%":
                x = stack.pop()
                y = stack.pop()
                if x == "0":
                    stack.append("0")
                else:
                 stack.append(y%x)
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