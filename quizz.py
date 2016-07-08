####problem 6####
def flatten(aList):
    '''
        aList: a list
        Returns a copy of aList, which is a flattened version of aList
        '''
    if isinstance(aList, list): #isinstance return True if aList is list
        if len(aList) == 0:
            return []
        first, rest = aList[0], aList[1:]
        return flatten(first) + flatten(rest)
    else:
        return [aList]

print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])



####problem 7####
def dict_interdiff(d1, d2):
    '''
        d1, d2: dicts whose keys and values are integers
        Returns a tuple of dictionaries according to the instructions above
        '''
    # inter: dictionary. keys: keys that are common in both d1 and d2.
    # values: result of applying f to values of inter's keys.
    inter = {}
    # diff: dictionary with only d1 elements and only d2 elements
    diff = {}
    
    for key in d1.keys():
        if key in d2:
            inter[key] = f(d1[key], d2[key])
        else:
            diff[key] = d1[key]

    for key in d2:
        if key not in inter:
            diff[key] = d2[key]
    
    return (inter, diff)

def f(a, b):
    return a > b

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print dict_interdiff(d1, d2)


####problem 8####
def f(s):
    return 'a' in s

def satisfiesF(L):
    """
        Assumes L is a list of strings
        Assume function f is already defined for you and it maps a string to a Boolean
        Mutates L such that it contains all of the strings, s, originally in L such
        that f(s) returns True, and no other elements. Remaining elements in L
        should be in the same order.
        Returns the length of L after mutation
        """

    L_new = []
    for s in L:
        if f(s) == True:
            L_new.append(s)

    L[:] = L_new
    return len(L_new)


L = ['a', 'b', 'a']
print satisfiesF(L)
