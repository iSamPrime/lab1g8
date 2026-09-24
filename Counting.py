stopWords=[]  # we initiate an empty list
words=["test", "hello", "what", "are", "you", "doing", "what", "test", "test"] # test list
def countWords(words, stopWords):
    with open('eng_stopwords.txt', 'r') as file: # file is opened and read
            for line in file: # we iterate through every line
                stopWords.append(line) # we add the word that line to the list via the operation "append"
                stopWords = [stopWords.replace("\n", "") for stopWords in stopWords] # we tidy up the list
                                                                            
            dict={} # we initiate an empty dictionary
            for w in words: # "for every word in the list of words"
                if w in stopWords: # "if that word also happens to be in the list stopWords"
                    continue # we continue (we ignore it)

                else:
                    dict[w] = dict.get(w,0) + 1 # if word is not already in dict, it is added
                                                # with an initial value of 1, all other occurances
                                                # raise the current value by 1
    print(dict)
countWords(words, stopWords)















#file=open("eng_stopwords.txt", "r")
#stopWords=file.read()
#for word in words:
#if word == #a value from stopWord, ignore it

        #elif word/= #a value from stopWord, 
            #dict["#"]=str(word)




