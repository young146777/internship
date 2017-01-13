import frequencyanalysis

f = open("../tempfile")
msg = f.read()
msg = msg.replace(" ", "")
msg = msg.replace('\n', "")
f.close()

letterlist = frequencyanalysis.letterfreq(msg)
lastitem = (0,0)
for item in letterlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
print('\n')

numlist = frequencyanalysis.numberfreq(msg)
lastitem = (0,0)
for item in numlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
print('\n')


wordlist = frequencyanalysis.wordfreq(msg, 2)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
print('\n')

wordlist = frequencyanalysis.wordfreq(msg, 3)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
print('\n')

wordlist = frequencyanalysis.wordfreq(msg, 4)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
wordlist = frequencyanalysis.wordfreq(msg, 5)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
wordlist = frequencyanalysis.wordfreq(msg, 6)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
wordlist = frequencyanalysis.wordfreq(msg, 7)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  
wordlist = frequencyanalysis.wordfreq(msg, 8)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  

wordlist = frequencyanalysis.wordfreq(msg, 12)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  


wordlist = frequencyanalysis.wordfreq(msg, 16)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  


wordlist = frequencyanalysis.wordfreq(msg, 20)
lastitem = (0,0)
for item in wordlist:
    if lastitem[1] != item[1]:
        print('\n')
    if item[1] != 1:
        print "%s:%s" % item,
    lastitem = item  


