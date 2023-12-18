

import random


def interpret(code):
    output = ""
    stack = []
    x=0
    y=0
    difY = 1
    difX = 0
    stringMode = False

    code = code.split('\n')
    for i in range(0,len(code)):
        code[i] = [*code[i]]

    while(code[x][y] != '@'):
        if stringMode:
            if code[x][y] == '\"':
                stringMode = False
            else:
                stack.append(ord(code[x][y]))
        else:
            match code[x][y]:
                case ' ':
                    nothing = 0
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    a = stack.pop()
                    stack.append(stack.pop() - a)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    a = stack.pop()
                    stack.append(stack.pop() / a)
                case '%':
                    a = stack.pop()
                    b = stack.pop()
                    if a == 0:
                        stack.append(0)
                    else:
                        stack.append(b%a)
                case '!':
                    if stack.pop == 0:
                        stack.append(1)
                    else:
                        stack.append(0)
                case '`':
                    if stack.pop() < stack.pop():
                        stack.append(1)
                    else:
                        stack.append(0)
                case '>':
                    difY = 1
                    difX = 0
                case '<':
                    difY = -1
                    difX = 0
                case '^':
                    difY = 0
                    difX = -1
                case 'v':
                    difY = 0
                    difX = 1
                case '?':
                    match random.randrange(0,4):
                        case 0:
                            difY = 1
                            difX = 0
                        case 1:
                            difY = -1
                            difX = 0
                        case 2:
                            difY = 0
                            difX = -1
                        case 3:
                            difY = 0
                            difX = 1
                case '_':
                    if stack.pop() == 0:
                        difY = 1
                        difX = 0
                    else:
                        difY = -1
                        difX = 0
                case '|':
                    if stack.pop() == 0:
                        difX = 1
                        difY = 0
                    else:
                        difX = -1
                        difY = 0
                case '\"':
                    stringMode = True
                case ':':
                    if len(stack) == 0:
                        stack.append(0)
                    else:
                        a = stack.pop()
                        stack.append(a)
                        stack.append(a)
                case '\\':
                    match len(stack):
                        case 1:
                            stack.append(0)
                        case 0:
                            stack.append(0)
                            stack.append(0)
                        case _:
                            a = stack.pop()
                            b = stack.pop()
                            stack.append(a)
                            stack.append(b)
                case '$':
                    stack.pop()
                case '.':
                    output += str(stack.pop())
                case ',':
                    output += chr(stack.pop())
                case '#':
                    x += difX
                    y += difY
                case 'p':
                    a = stack.pop()
                    b = stack.pop()
                    code[b][a] = stack.pop()
                case 'g':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(ord(code[a][b]))
                case _:
                    stack.append(int(code[x][y]))
        
        x += difX
        y += difY

    # TODO: Interpret the code!
    return output

#print(interpret("08>:1-:v v *_$.@\n  ^    _$>\:^"))
#print(interpret("01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"))
print(interpret("2>:3g\" \"-!v\  g30          <\n |!`\"&\":+1_:.:03p>03g+:\"&\"`|\n @               ^  p3\\\" \":<\n2 2345678901234567890123456789012345678"))