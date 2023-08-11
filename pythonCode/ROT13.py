def rot13(message):
    out = ""
    for  elen in message:
        if elen.isalpha():
            if elen.isupper():
                if ord(elen) + 13 > 90:
                    out += chr(ord(elen) - 13)
                else:
                    out += chr(ord(elen) + 13)
            else:
                if ord(elen) + 13 > 122:
                    out += chr(ord(elen) - 13)
                else:
                    out += chr(ord(elen) + 13)
        else: 
            out += elen
    return out
