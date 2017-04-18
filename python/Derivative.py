# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 16:46:31 2015
"""
'''Quick little program I wrote in 40 minutes'''
def derivative(func):
    finalString = ""
    parts = []
    newParts = []
    symbols = []
    if all(i not in "*/" for i in func): #Doesn't do divisional coefficients yet
        for place, symb in enumerate(func):
            if symb in "+-":
                symbols.append(symb)
                """Alright these two lines look really hard and I should've"""
                """Made them longer but I did what I did and I have no     """
                """Regrets. I had to make them this way because I used an  """
                """Enumerate to loop through the function, and it couldn't """
                """Be updated while looping through it. I used an enumerate"""
                """So that I could ensure I was cutting off at the right   """
                """Spot. Anyway, one line at a time documentation          """
                parts.append(func[:place-sum(len(i)+1 for i in parts)])
                """This appends the function, from the very beginning to   """
                """Where the place value says to stop. However, the place  """
                """Value is according to the function, which is changed    """
                """Below. So we have to subtract from the place value      """
                """Since the function is now shorter based on the length of"""
                """Each item that's already in the parts list, adding one  """
                """To account for the symbol that goes to the other list   """
                func = func[place-sum(len(i)+1 for i in parts[:-1])+1:]
                """This function updates it in a similar fashion, except it"""
                """Starts where the previous one ended, and skips the most """
                """Recent element of the parts list because that's the part"""
                """Being chopped off, and add one to remove the symbol"""
        parts.append(func)
        for i in parts:
            if "^" in i:
                term = i.split("^") #term[0] is coefficient and x, term[1] is power
                coeff = int(term[0][0])*int(term[1]) #Multiply coefficient and power
                power = int(term[1])-1 #Yes this will print out ax^1 but I don't care
                newParts.append(str(coeff)+'x^'+str(power))
            else:
                if 'x' not in i:
                    continue
                else:
                    if len(i) == 1: #Means that it's just x
                        newParts.append('1')
                    else:
                        newParts.append(i[:i.index('x')]) #Append start until x is reached
        for val, i in enumerate(newParts[:-1]):#Stop before the last element
            finalString += i
            finalString += symbols[val]
        finalString += newParts[-1]
        print finalString
    
derivative("7x^4+9x^3-4x^2+x-5")