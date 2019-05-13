def sentenceHandler(data):
    words =  data.split()
    new = ""
    i =0
    check = len(words)
    while(i<check):
        if i == check:
            break
        if words[i] == "greater":
            i +=1
            if i !=check and words[i]== "than":
                i+=1
                new = new+ " >"
                if i != check and words[i] == "or":
                    new = new+ "="
                    i+=3
        elif words[i] =="less":
            i+=1
            if i !=check and words[i]== "than":
                i+=1
                new = new+ " <"
                if i != check and words[i] == "or":
                    new = new+ "="
                    i+=3
        elif words[i] == "equal" or words[i] == "equals":
            i+=1
            if words[i] == "to":
                new = new +" == "
                i+=1
        elif words[i] == "not":
            i+=1
            if words[i] == "equal" or words[i] == "equals":
                i+=1
                if words[i] == "to":
                    new = new +" == "
                    i+=1
        else:
            new = new +" " +words[i]
            i+=1
    return new
