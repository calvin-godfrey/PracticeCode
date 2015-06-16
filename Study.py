import bs4, requests, re, random
#Only thing that changes in each URL
pages = ['121', '122', '123', '124', '125', '126', '310', '312', '313', '314', '315', '316', '420', '421', '422', '500']
right = 0
total = 0
#All the string before the page index in the URL
before = "http://conjuguemos.com/print_vocabulary_list.php?id="
#List that will hold vocab
vocab = []
#Everything after page in URL
after="&source=public"

for i in pages: #For each page to get vocab from
    site = requests.get(before + i + after)
    site.raise_for_status() #Make sure it got everything correctly
    soup = bs4.BeautifulSoup(site.text) #Make the text readable, not just object
    ####################################################
    #Regex object searching text for specific subject  #
    #Searches for one or more digit (\d+)              #
    #Then one or more of anything (.+)                 #
    #Until it finds a '<' symbol, meaning it's the end #
    #Of that vocab term                                #  
    ####################################################
    regex = re.compile("\d+\..+<")
    words = regex.findall(str(soup)) #Creates list of all instances of the regex
    for i in words:
        words[words.index(i)] = i[:-1] #Removes open carot symbol
    for i in range(0, len(words), 2):
        vocab.append([unicode(words[i], "utf-8"), unicode(words[i+1], "utf-8")]) #Converts to unicode (accents) and pairs english/spanish
                
    print "DONE WITH PAGE"

while True:
    total += 1.0 #Another question asked
    x = random.randint(0, len(vocab)+1) #Pick random vocab word
    print x[0]
    x = raw_input("Answer:\n> ")
    if x.lower() == x[1].lower(): #Right answer
        print "Woo"
        right += 1.0
    else:
        print "Wrong"
        print x[1]
        
    print "Accents: áéíóúñ" #To help people get those right
    print "Score: " + str(right/total)