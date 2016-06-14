print "Please think of a number between 0 and 100!"

x = 50
epsilon = 0.01
low = 0.0
high = 100.0
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print "Is your secret number "+ str(int(ans)) +"?"
    y = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if y not in ['l','h','c']:
        print "Sorry, I did not understand your input."
    
    if y == 'l': #ans**2 < x:
        low = int(ans)
    elif y == 'h':
        high = int(ans)
    elif y == 'c':
        break
    
    ans = (high + low)/2.0

print "Game over. Your secret number was: "+ str(int(ans))