states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
states = [i.lower() for i in states]
words = [line.strip() for line in open("", "r")] #Change for you

end = filter(None, [word + " " + state if len(filter(None, [state if all([i not in state for i in word]) else '' for state in states]))==1 else '' for word in words])

print len(end)
##################################################
#This program creates a list of all words that   #
#Have exactly one state with no letters in common#
#For example, mackerel and ohio have nothing in  #
#Common, and so do aaron and mississippi.        #
#Really proud of this one liner                  #
##################################################

'''answer = file("final.txt", "w") #UNCOMMENT TO SAVE
for i in end:
    answer.write(i)
    answer.write("\n")'''
