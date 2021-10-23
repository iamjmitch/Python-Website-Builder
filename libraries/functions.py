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
                print(yellow("Please enter 'yes' or press the enter key to skip"))
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

def yellow(message):
    return '{.Yellow}{message}{.ResetAll}'.format(textColors,textColors, message=message)

def red(message):
    return '{.Red}{message}{.ResetAll}'.format(textColors,textColors, message=message)

def green(message):
    return '{.Green}{message}{.ResetAll}'.format(textColors,textColors, message=message)

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
            imgSrc = question("Image Source URL")
            alt = question("Image Description")            
            html =('<img src="{imgSrc}" alt="{alt}" width="500" height="auto">'.format(alt = alt, imgSrc=imgSrc))            
        elif tag == "h1":
            text = question("Heading Text")
            html = "<h1>"+text+"</h1>"       
        else:
            if tag == "":
                print(red("Element Selection Cannot Be Left Blank"))
            else:
                print(red("'"+tag + "' Is An Invalid Element Tag. "))
                print(yellow("Please choose from:\n1: a\n2: p\n3: h1\n4: img"))
            tag = question("Enter Element Type")      
    
    print(html)
    return(html)


