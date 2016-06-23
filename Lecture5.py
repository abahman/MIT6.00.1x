def iterPower(base, exp):
    '''
        base: int or float.
        exp: int >= 0
        
        returns: int or float, base^exp
        '''
    if exp == 0.0:
        return 1.0
    else:
        result = 1.0
        while (exp > 0.0):
            result *= abs(base)
            exp -= 1
        if base > 0.0:
            return result
        elif base < 0.0:
            return -result


def isPalindrome(s):
    '''
    This is finding if the string is palindrome or not
    '''
    def toChars(s): #convert upercase to lower and remove spaces
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):   #fuction that slice and check for palindrome
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


####from a problem in Lecture 6
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

####problem in lecture 6
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