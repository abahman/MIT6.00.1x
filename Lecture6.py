def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print applyEachTo([inc, square, halve, abs], -3)



def biggest(aDict):
    '''
        aDict: A dictionary, where all the values are lists.
        
        returns: The key with the largest number of values associated with it
        '''
    res = {}
    for i in aDict:
        res[i]=len(aDict[i])
    
    for j in res.keys():
        if res[j] == max(res.values()):
            return j


print biggest({'a': [15, 13, 12], 'b': [13, 6]})