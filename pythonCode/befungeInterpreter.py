

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
            case '':
                break
            case '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
                break
            case '-':
                stack.append(int(stack.pop()) - int(stack.pop()))
                break
            case '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
                break
            case '/':
                stack.append(int(stack.pop()) / int(stack.pop()))
                break
            case '%':
                x = stack.pop()
                y = stack.pop()
                if x == '0':
                    stack.append('0')
                else:
                 stack.append(y%x)
                break
            case '!':
                if stack.pop == '0':
                    stack.append('1')
                else:
                    stack.append('0')
                break
            case '`':
                if stack.pop() < stack.pop():
                    stack.append('1')
                else:
                    stack.append('0')
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
                if stack.pop() == '0':
                    difx = 1
                    dify = 0
                else:
                    difx = -1
                    dify = 0
                break
            case '|':
                if stack.pop() == '0':
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
                x = stack.pop()
                stack.append(x)
                stack.append(x)
                break
            case '\\':
                
                break
            case '$':
                break
            case '.':
                break
            case ',':
                break
            case '#':
                break
            case 'p':
                break
            case 'g':
                break
        
        x += difX
        y += difY

    # TODO: Interpret the code!
    return output