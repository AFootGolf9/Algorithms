if s == "" :return False
    char = 1
    out = "#"
    captal = True
    for elem in s:
        if elem == ' ':captal = True
        elif captal :
            out += elem.upper()
            captal = False
            char += 1
        else : 
            out += elem.lower()
            char += 1
        if char == 140 : return False
    return out
