

import random


def interpret(code):
    output = ""
    stack = []
    x=0
    y=0
    difY = 1
    difX = 0

    code = code.split('\n')

    while(code[x][y] != '@'):
        match code[x][y]:
            case ' ':
                nothing = 0
            case '+':
                stack.append(stack.pop() + stack.pop())
            case '-':
                stack.append(stack.pop() - stack.pop())
            case '*':
                stack.append(stack.pop() * stack.pop())
            case '/':
                stack.append(stack.pop() / stack.pop())
            case '%':
                a = stack.pop()
                b = stack.pop()
                if x == 0:
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
                if len(stack )== 0:
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
                output += stack.pop()
            case ',':
                output += ord(stack.pop())
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
                stack.append(code[b][a])
            case _:
                stack.append(code[x][y])
        
        x += difX
        y += difY

    # TODO: Interpret the code!
    return output

print(interpret(">987v>.v\nv456<  :\n>321 ^ _@"))