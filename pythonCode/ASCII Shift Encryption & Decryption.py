def ascii_encrypt(plaintext):
    out = ""
    for i in range(len(plaintext)):
        out += chr(ord(plaintext[i]) + i)
    return out
    
def ascii_decrypt(encrypted):
    out = ""
    for i in range(len(encrypted)):
        out += chr(ord(encrypted[i]) - i)
    return out
