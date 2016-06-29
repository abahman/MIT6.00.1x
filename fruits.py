def nfruits(FruitDict,pattern):
    '''
        function nfruits that takes two inputs:
        FruitDict : A non empty dictionary containing type of fruit
        and its quantity initially with Python when he leaves home (any length).
        e.g {'A': 1, 'B': 2, 'C': 3}
        pattern: A string pattern of the fruits eaten by Python on his journey
        e.g 'AC'
        
        function returns maximum quantity out of the different types of fruits
        that is available with Python when he has reached the campus
        '''

    for i in range(len(pattern)):
        FruitDict[pattern[i]] -= 1    #reduce 1 from consumed fruit key in FruitDict
        
        FruitDict_copy = FruitDict.copy()    #generate a copy of FruitDict for manupulation
        del FruitDict_copy[pattern[i]]   #delete the fruit key that consumed (in FruitDict_copy only)
        
        if i == len(pattern)-1:   #break the loop if reached last element to avoid counting for update value
            break
        
        for j in FruitDict_copy:    #for loop to update FruitDict with unconsumed fruit key
            if j in FruitDict:
                FruitDict[j] += 1


    return max(FruitDict.values())    #return the maximum value in FruitDict

print nfruits({'H': 9, 'J': 5, 'O': 7, 'N': 5, 'P': 5, 'T': 6, 'Y': 10, 'X': 8}, 'P')
print nfruits({'J': 6, 'U': 5, 'O': 6, 'F': 10}, 'FJUU')
print nfruits({'D': 7, 'G': 7, 'F': 6, 'L': 5, 'N': 6, 'P': 6, 'T': 8, 'X': 5}, 'TT')