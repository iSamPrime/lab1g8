def printTopMost(frequencies,n): 
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1],reverse=True) 
    for i in range(n):
        word, value = sorted_frequencies[i]
        print(word.ljust(20),str(value).rjust(5))
        
