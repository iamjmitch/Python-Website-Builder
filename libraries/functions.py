import os
from libraries.colors import textColors
from shutil import copyfile

# -- Quality of life
true = True
false = False

#all in one question asker 
def question(text, trueOrFalse = false):
    yesNoCheck = False
    while yesNoCheck == False:
        formatted = '{.Green}{text}: {.ResetAll}'.format(textColors, textColors, textColors, text=text)
        userInput = input(formatted)
        userInput = userInput.lower()    
        if trueOrFalse == true:
            if "yes" in userInput or "true" in userInput:
                return True
                yesNoCheck = true
            elif "no" in userInput or "false" in userInput:
                return False
                yesNoCheck = true        
            elif userInput == "":                
                return False
                yesNoCheck = true
            else:
                printWarning("Please enter 'yes' or press the enter key to skip")
        else:
            yesNoCheck = true
            return userInput


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

#Housekeeping
def cleanHtml():
    if question("Clean HTML? ", true) == true:
        copyfile('index_clean.html', 'index.html')  




# -- Error Reporting --

#print yellow message in console
def printWarning(message):
    print('{.Yellow}{message}{.ResetAll}'.format(textColors,textColors, message=message))

#print red message in console
def printError(message):
    print('{.Red}{message}{.ResetAll}'.format(textColors,textColors, message=message))

#print green message in console
def printSystemMessage(message, printOnLineAbove = false):
    if printOnLineAbove == false:
        
        print('\x1b[1A\x1b[2K')
    print('{.Yellow}{message}{.ResetAll}'.format(textColors,textColors, message=message))
    
# Combine all available html sections for error display
def appendPossbileSections(options):
    temp = ""
    for i in range(len(options)):
        temp = temp + '{.Yellow}{number}: {.White}"{selection}"'.format(textColors,textColors, number = str(i+1), selection= options[i])        
        if i+1 < len(options):
            temp = temp + "\n"
    return temp

# -- Use Functions --

def tagMaker(tag):
    html = ""
    while html == "":
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
        elif tag == "img":
            pass
        elif tag == "h1":
            pass        
        else:
            if tag == "":
                printWarning("Element Selection Cannot Be Left Blank")
            else:
                printWarning("'"+tag + "' Is An Invalid Element Tag")
            tag = question("Enter Element Type")      
    
    print(html)
    return(html)


