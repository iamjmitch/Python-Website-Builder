from libraries.colors import textColors
# -- Helper functions
#Add white space left
def awsl(string, count): 
    tempString = string
    for i in range(count):
        tempString = " "+tempString
    return tempString

#Add white space right
def awsr(string, count): 
    tempString = string
    for i in range(count):
        tempString = tempString+" "
    return tempString

def appendPossbileSections(options):
    temp = ""
    for i in range(len(options)):
        temp = temp + '{.Yellow}{number}: {.White}"{selection}"'.format(textColors,textColors, number = str(i+1), selection= options[i])        
        if i+1 < len(options):
            temp = temp + "\n"
    return temp

 

