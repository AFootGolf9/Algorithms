

import random


def interpret(code):
    output = ""
    stack = []
    x=0
    y=0
    difX = 1
    difY = 0

    while(code[x][y] != '@'):
        match(code[x][y]):
            case ' ':
                break
            case '+':
                stack.append(stack.pop() + stack.pop())
                break
            case '-':
                stack.append(stack.pop() - stack.pop())
                break
            case '*':
                stack.append(stack.pop() * stack.pop())
                break
            case '/':
                stack.append(stack.pop() / stack.pop())
                break
            case '%':
                a = stack.pop()
                b = stack.pop()
                if x == 0:
                    stack.append(0)
                else:
                    stack.append(b%a)
                break
            case '!':
                if stack.pop == 0:
                    stack.append(1)
                else:
                    stack.append(0)
                break
            case '`':
                if stack.pop() < stack.pop():
                    stack.append(1)
                else:
                    stack.append(0)
                break
            case '>':
                difX = 1
                dify = 0
                break
            case '<':
                difX = -1
                dify = 0
                break
            case '^':
                difX = 0
                dify = -1
                break
            case 'v':
                difX = 0
                dify = 1
                break
            case '?':
                match(random.randrange(0,4)):
                    case 0:
                        difX = 1
                        dify = 0
                        break
                    case 1:
                        difX = -1
                        dify = 0
                        break
                    case 2:
                        difX = 0
                        dify = -1
                        break
                    case 3:
                        difX = 0
                        dify = 1
                        break
                break
            case '_':
                if stack.pop() == 0:
                    difx = 1
                    dify = 0
                else:
                    difx = -1
                    dify = 0
                break
            case '|':
                if stack.pop() == 0:
                    dify = 1
                    difx = 0
                else:
                    dify = -1
                    difx = 0
                break
            case '\"':
                stringMode = True
                break
            case ':':
                a = stack.pop()
                stack.append(a)
                stack.append(a)
                break
            case '\\':
                match(stack.length()):
                    case 1:
                        stack.append(0)
                        break
                    case 0:
                        stack.append(0)
                        stack.append(0)
                        break
                    case _:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a)
                        stack.append(b)
                break
            case '$':
                stack.pop()
                break
            case '.':
                output += stack.pop()
                break
            case ',':
                output += ord(stack.pop())
                break
            case '#':
                x += difX
                y += dify
                break
            case 'p':
                a = stack.pop()
                b = stack.pop()
                code[b][a] = stack.pop()
                break
            case 'g':
                a = stack.pop()
                b = stack.pop()
                stack.append(code[b][a])
                break
            case _:
                stack.append(code[x][y])
        
        x += difX
        y += difY

    # TODO: Interpret the code!
    return output
