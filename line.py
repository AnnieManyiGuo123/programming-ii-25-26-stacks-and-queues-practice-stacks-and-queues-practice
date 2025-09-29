def lunch_line():
    line = ["a","b","c","d"]
    while True: 
        new = input ("new person in the line: ")
        if new != '':
            line.append(new)
        line.pop(0) 
        if len(line) > 0:
            print (line)
        elif len(line) == 0:

            print ("everyone is done!")
            
            return 
        
lunch_line()
    
        
