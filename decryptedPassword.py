def decryptPassword(s):
    # Write your code here
    decrypted= ""
    numbers = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if s[i] == "0": decrypted += s[i]
            else:numbers += s[i]
            i += 1; continue
        
        if i <= (len(s)-3):
            if (s[i].isupper() and s[i+1].islower() and s[i+2] == "*"):
                decrypted += (s[i+1] + s[i])
                i += 3
                continue
        
        decrypted += s[i]
        i += 1
    
    for number in numbers[-1::-1]:
        decrypted = decrypted[:decrypted.find("0")] + number + decrypted[decrypted.find("0")+1:]

    return decrypted

print(decryptPassword("51Pa*0Lp*0e"))
print(decryptPassword("pTo*Ta*O"))