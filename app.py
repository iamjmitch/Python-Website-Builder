# -- Libraries
import os
import re
from libraries import colors
from libraries import functions
from libraries.functions import *

# ---------------------Variables ---------------------------

# -- System Variables
textColors = colors.textColors 

# -- File locations
inputFileLocation = "index.html"
outputFileLocation = "tempIndex.html"

# -- Global variables
currentPosition = ""
indent = 0
possibleSections = ['section1','section2', 'section3']


# ---------------------Start Actual App ---------------------

# -- Get injection section
print('\n{.Bold}Enter Section:{.ResetAll}'.format(textColors, textColors))
section = input()
# Check if section is allowed and if not valid, exit
if section not in possibleSections:    
    print ('{.Red}\n----------------- ERROR------------------\n\nYour Inputted Section {.White}{SELECTION}{.Red} Does Not Exist\n'.format(textColors,textColors,textColors, SELECTION = "'" +section + "'"))
    print ('{.Yellow}{Message}{.White}{Options}'.format(textColors, textColors, Message = "Please Choose From The Following Sections:\n", Options = appendPossbileSections(possibleSections)))
    print ('{.Red}\n------------ EXITING PROGRAM ------------\n{.ResetAll}'.format(textColors, textColors))
    exit()

# -- Get Injection Element
print('{.Bold}Enter Element Type:{.ResetAll}'.format(textColors, textColors))
element = input()

# -- Get injection phrase
print('{.Bold}Enter Phrase:{.ResetAll}'.format(textColors, textColors))
phrase = input()

# read contents of input file 
inputfile = open(inputFileLocation, 'r').readlines()

# Create temp file to output
with open(outputFileLocation,'w') as write_file:
    for line in inputfile: 
        #tracks line indentation
        indent = len(line) - len(line.lstrip(' ')) 

        # Update element counter
        if "<!-- line" in line:
            currentPosition = re.sub('\D', '', line)
            write_file.write(line)
       
        elif section in line: # Search if current section matches user iputted section for injection
            currentPosition = str(int(currentPosition)+1)
            string = awsl('<!-- line'+currentPosition+' -->\n', indent) + awsl('<p>'+phrase+'</p> \n', indent) # Premake injection string adding whitespace           
            write_file.write(string) # Write injection to file
            write_file.write(line)
        else:
            write_file.write(line)

print ('{.Green}-- Data Added Successfully --\n{.ResetAll}'.format(textColors, textColors))

# Cleanup
os.remove(inputFileLocation) # Delete input file
os.rename(outputFileLocation, inputFileLocation) # Replace input file with temp

