def getSecondLastWord(s):
    s= s.strip()
    wordCounter = 0
    word = ""
    for x in reversed(s):
        if x == " ":
            wordCounter +=1
            if wordCounter == 2:
                return word
            else:
                word = ""

        word = x + word
    
    wordCounter += 1
    if wordCounter == 2:
        return word
    
    return ""
    
    
def main():
    binary = "Good one aditya!"
    print getSecondLastWord(binary)

main()
