'''
Created on 2016. 7. 27.
@author: mulder
'''

def anagram(firstString, secondString):
    firstList = sorted(list(firstString))
    secondList = sorted(list(secondString))

    if len(firstList) != len(secondList):
        return False
    else:
        if firstList == secondList:
            return True
        else:
            return False        
    
print(anagram('heart', 'earth'))

def anagramBruteForce(firstInput, secondInput):
    firstInputList = list(firstInput)
    secondInputList = list(secondInput)
    
    for i in range(len(firstInputList)):
        for j in range(len(secondInputList)):
            if firstInputList[i] == secondInputList[j]:
                secondInputList[j] = ""
    tempList = "".join(secondInputList)
    if tempList == "":
        return True
    else:
        return False

print(anagramBruteForce('hhhooo', 'ooohhh'))
    
