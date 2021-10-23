from libraries.colors import textColors
from libraries.functions import *

def sectionErrorCheck(section, possibleSections):
    if section not in possibleSections:    
        print ('{.Red}\n----------------- ERROR------------------\n\nYour Inputted Section {.White}{SELECTION}{.Red} Does Not Exist\n'.format(textColors,textColors,textColors, SELECTION = "'" +section + "'"))
        print ('{.Yellow}{Message}{.White}{Options}'.format(textColors, textColors, Message = "Please Choose From The Following Sections:\n", Options = appendPossbileSections(possibleSections)))
        print ('{.Red}\n------------ EXITING PROGRAM ------------\n{.ResetAll}'.format(textColors, textColors))
        return false
    else:
        return true