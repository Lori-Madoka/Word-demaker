# solo project ftwv
# i want to make a program that can swap the letters of a word randomly except for the first and last letter of a word.
import random

def typo(input):
    temp = ''
    toparse = list(input) #convert input string to a list of characters even though thats what a string is but python cant reason that.
    startofwordglobalindex = 0
    wordlength = 0
    endofwordglobalindex = 0
    copyofglobalindex = 0
    currentposinword = 0
    currentposinglobal = 0
    randomchar = 0
    while currentposinglobal < len(input):
        if toparse[currentposinglobal] != ' ' and toparse[currentposinglobal] != ',' and toparse[currentposinglobal] != '.' and toparse[currentposinglobal] != ':' and toparse[currentposinglobal] != ';' and toparse[currentposinglobal] != '!' and toparse[currentposinglobal] != '?' and toparse[currentposinglobal] != '"' and toparse[currentposinglobal] != '(' and toparse[currentposinglobal] != ')': #while it doesnt encounter a space (or rather a new word) it will continue through the current word
            startofwordglobalindex = currentposinglobal
            currentposinword = currentposinglobal
            tempposinglobal = currentposinglobal
            while toparse[tempposinglobal] != ' ' and toparse[tempposinglobal] != '.' and toparse[tempposinglobal] != '!' and toparse[tempposinglobal] != '"' and toparse[tempposinglobal] != ';' and toparse[tempposinglobal] != ':' and toparse[tempposinglobal] != '(' and toparse[tempposinglobal] != ')' and toparse[tempposinglobal] != '?': #this loop will iterate through the string until it reaches a space or punctuation mark where it is obvious that the word has ended
                tempposinglobal+=1
            #setting variables to prepare for individual letter swapping in the word
            endofwordglobalindex = tempposinglobal #sets the upper limit for the random function
            wordlength = tempposinglobal - startofwordglobalindex
            currentposinword = startofwordglobalindex + 1
            endofwordglobalindex = tempposinglobal - 2
            for i in range(startofwordglobalindex, endofwordglobalindex): #this loop will iterate though the word within the index bounds to swap each of the letters randomly.
                randomchar = startofwordglobalindex + (random.randint(1, wordlength-2))
                temp = toparse[randomchar] #store this character so it is not lost when replaced
                toparse[randomchar] = toparse[currentposinword] #replace the random character with the one from the current index in the word
                toparse[currentposinword] = temp
                currentposinword+=1 #move to the next character in the list
            currentposinglobal = tempposinglobal #update the main position index after the operation has finished, separate variables to ensure no corruption of the main position index.
            wordlength=0
        else:
            currentposinglobal+=1
    finish = toparse
    return finish

def main():
    #the main function that will call all other functions
    userinput = input("Gimme Gimme string: ") #take the user's initial string
    print("original string = ", userinput)
    finallist = typo(userinput)
    print("string has been converted below: \n")
    finalstring = "".join(finallist) #joining the de-ai-comprehensible list of characters to a string to make the output human-readable
    print(finalstring)

main()
