def solution(s):
    out = ""
    for elem in s :
        if (ord(elem) >= 65 and 90 >= ord(elem)):
            out += " " + str(chr(ord(elem)))
        else : out += str(elem)
    
    return out
