import pyttsx3

def sentenceHandler(data):
    w =  data.lower().split()
    new = ""
    i =0
    check = len(w)
    try:
    
        while(i<check):
            if i == check:
                break
            if w[i] == "greater":
                i +=1
                if i !=check and w[i]== "than":
                    i+=1
                    new = new+ " >"
                    if i != check and w[i] == "or":
                        new = new+ "="
                        i+=3
            elif w[i] =="less":
                i+=1
                if i !=check and w[i]== "than":
                    i+=1
                    new = new+ " <"
                    if i != check and w[i] == "or":
                        new = new+ "="
                        i+=3
            elif w[i] == "equal" or w[i] == "equals":
                i+=1
                if w[i] == "to":
                    new = new +" == "
                    i+=1
            elif w[i] == "not":
                i+=1
                if w[i] == "equal" or w[i] == "equals":
                    i+=1
                    if w[i] == "to":
                        new = new +" == "
                        i+=1
            elif w[i] == 'or' or w[i]== 'and' or w[i] == '+' or w[i] == "-" or w[i] =="*" or w[i] == "%" or w[i] == '/':
                new = new + " "+ w[i]
                i +=1
            elif w[i] == 'plus':
                i +=1
                new = new +" + "
            elif w[i] == 'minus':
                i +=1
                new = new +" - "
            elif w[i] == 'multiplication' or w[i] == "multiply":  
                i +=1
                new = new +" * "
            elif w[i] == "modulo":
                i+=1
                new = new + " % "
            elif w[i] == "by":
                i+=1
                new = new + " / "
            elif w[i] == "divide":
                i+=1
                new = new + " // "
            elif w[i] == "bitwise":
                i+=1
                if w[i] == 'complement':
                    new = new+ " ~"
                    i+=1
                elif w[i] == "and":
                    new = new+ ' &'
                    i+=1
                elif w[i] == "and":
                    new = new+ ' &'
                    i+=1
                elif w[i] == "exclusive":
                    i+=1
                    if w[i] == 'or':
                        new = new+ " ^"
                        i+=1
                elif w[i] == 'or':
                    new = new+ ' |'
                    i+=1
                elif w[i] == "shift":
                    i+=1
                    if w[i] == 'left':
                        new = new+ " << "
                        i+=1
                    elif w[i] == 'right':
                        new = new + " >> "
                        i+=1
            elif w[i] == "of":
                i+=1
                new = new+"["+ w[i]+"]"
                i+=1
            elif w[i] == 'next' and w[i+1] == 'line':
                new = new+'\n'
                i+=2
            elif w[i] == 'tab':
                new= new+ "\t"
                i+=1
            elif w[i] == "colon":
                    new = new+ ': \n\t'
                    i+=1
            else:
                new = new +" " +w[i]
                i+=1
    except:
        speak("Incorrect string format.... speak single string at once")
        return ""
    return new

def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()
