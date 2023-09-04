def snail(snail_map):
    startH = 0
    startV = -1
    endH = len(snail_map)
    endV = endH
    modH = 0
    modV = 1
    H = 0
    V = 0
    out = []

    done = 0
    while(done < len(snail_map) * len(snail_map)):
        out.append(snail_map[H][V])
        done += 1
        if (H == endH - 1 and modH == 1):
            modH = 0
            modV = -1
            endH -= 1
        elif (V == endV - 1 and modV == 1):
            modH = 1
            modV = 0
            endV -= 1
        elif (H == startH + 1 and modH == -1):
            modH = 0
            modV = 1
            startH += 1
        elif (V == startV + 1 and modV == -1):
            modH = -1
            modV = 0
            startV += 1
        H += modH
        V += modV
       
    return out
