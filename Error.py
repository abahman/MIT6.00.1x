def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    else:
        print "result is", result
    finally:
        print "executing finally clause"

def divideNew(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    except TypeError:
        divideNew(int(x), int(y))
    else:
        print "result is", result
    finally:
        print "executing finally clause"



def Normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers

try:
    Normalize([0, 0, 0])
except ZeroDivisionError, e:
    print 'Invalid maximum element'