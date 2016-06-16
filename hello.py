print 'hello, Ammar'
#print 1+1
#
#temp = '32'
#if temp > 85:
#    print "Hot"
#elif temp > 62:
#    print "Comfortable"
#else:
#    print "Cold"
#
#temp = 120
#if temp > 85:
#    print "Hot"
#elif temp > 100:
#    print "REALLY HOT!"
#elif temp > 60:
#    print "Comfortable"
#else:
#    print "Cold"


import sys
print (sys.version)

s = 'azcbobobegghakl'
count = 0

for i in range(len(s)):
    if s[i:].startswith('bob'):
        count += 1

print 'Number of vowels: '+ str(count)