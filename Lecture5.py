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