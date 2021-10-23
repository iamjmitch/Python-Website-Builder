import os
from libraries.colors import textColors
from shutil import copyfile

# -- Quality of life
true = True
false = False


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

def question(text, trueOrFalse = false):
    boolean = 2
    while boolean == 2:
        print('{.Bold}{text}:{.ResetAll}'.format(textColors, textColors, text=text))
        userInput = input()
        userInput = userInput.lower()    
        if trueOrFalse == true:            
            if "yes" in userInput or "true" in userInput:
                return True
                boolean = 1
            elif "no" in userInput or "false" in userInput:
                return False
                boolean = 0         
            elif userInput == "":
                return False
                boolean = 0
            else:
                printWarning("Please enter 'yes' or press the enter key to skip\n")
        else:
            boolean = 0 
            return userInput

def cleanHtml():
    if question("Clean HTML? ", true) == true:
        copyfile('index_clean.html', 'index.html')    

def printWarning(message):
    print('{.Yellow}{message}{.ResetAll}'.format(textColors,textColors, message=message))

def tagMaker(tag):
    html = ""
    #Link Tag
    if tag == "a":
        href = question("href")
        linkText = question("Link Text")        
        if "http://" not in href:
            href = "http://"+href
        if question("Open in new tab?", true) == true:
            html = '<a href="'+href+'" target="_blank">'+linkText+'</a>'
        else:
            html = '<a href="'+href+'">'+linkText+'</a>'  
    elif tag == "p":
        text = question("Paragraph Text")
        html = "<p>"+text+"</p>"
    print(html)
    return(html)


