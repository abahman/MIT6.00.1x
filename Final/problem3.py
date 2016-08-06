def dict_invert(d):
    '''
        d: dict
        Returns an inverted dictionary according to the instructions above
        '''
    e = {}
    
    for i in range(len(d)):
        if d.items()[i][1] in e:
            e[d.items()[i][1]].append(d.items()[i][0])
        else:
            e[d.items()[i][1]] = [d.items()[i][0]]

    for i in e.keys():
        e[i].sort()

    return e

#d = {1:10, 2:20, 3:30}
#d = {1:10, 2:20, 3:30, 4:30}
#d = {4:True, 2:True, 0:True}
#d = {8: 6, 2: 6, 4: 6, 6: 6}
d = {30000: 30, 600: 30, 2: 10}
#d = {0: 9, 9: 9, 5: 9}

#print dict_invert(d)