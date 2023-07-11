def reverse_words(text):
    txet = ""
    word = False
    wordHold = ""

    for i in range (0,len(text)):
        if(text[i] == " "):
            word = False
        else :
            word = True
        if(word):
            wordHold += text[i]
        else :
            hold = ""
            for elem in wordHold:
                hold = elem + hold
            txet += hold + " "
            wordHold = ""
    hold = ""
    for elem in wordHold:
        hold = elem + hold    
    txet += hold
    
    return txet
