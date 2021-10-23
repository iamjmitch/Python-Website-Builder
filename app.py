# -- Libraries
import os
import re
from libraries import colors
from libraries.functions import *
from libraries.errorChecks import *

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
cleanHtml()
#Get injection section
tagLocation = question("Enter Section")

#Check if section is valid
if tagLocation == "":
    tagLocation = "section1"    
if sectionErrorCheck(tagLocation, possibleSections) == false:
    exit()

#Get Injection Element and contents
elementType = question("Enter Element Type")

#Combine everything ready for injection
element = tagMaker(elementType)

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
       
        elif tagLocation in line: # Search if current section matches user iputted section for injection
            currentPosition = str(int(currentPosition)+1)
            string = awsl('<!-- line'+currentPosition+' -->\n', indent) + awsl(element +'\n', indent) # Premake injection string adding whitespace           
            write_file.write(string) # Write injection to file
            write_file.write(line)
        else:
            write_file.write(line)

print(green("-- Data Added Successfully --\n"))

# Cleanup
os.remove(inputFileLocation) # Delete input file
os.rename(outputFileLocation, inputFileLocation) # Replace input file with temp

