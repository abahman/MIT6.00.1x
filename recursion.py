def ndigits(x):
    '''
        The function takes integer x (either positive or negative)
        Then, it return the number of digits of integer x
    '''

    if x == 0:    #Base case 1
        return 0
    elif abs(x)/10 <= 0:    #Base case 2
        return 1
    else:    #Recursive step
        return 1 + ndigits(abs(x)/10)