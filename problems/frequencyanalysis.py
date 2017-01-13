import string
import operator

def letterfreq(msg):
    dic = {}
    for letter in string.lowercase:
        dic[letter] = msg.count(letter)
    freqlist = sorted(dic.items(), key=operator.itemgetter(1))
    return freqlist
def numberfreq(msg):
    dic = {}
    for number in string.digits:
        dic[number] = msg.count(number)
    freqlist = sorted(dic.items(), key=operator.itemgetter(1))
    return freqlist
def wordfreq(msg, length):
    dic = {}
    for i in range(0,len(msg)-length):
        word = msg[i:i+length]
        if '\n' in word: continue
        dic[word] = msg.count(word)
    freqlist = sorted(dic.items(), key=operator.itemgetter(1))
    return freqlist
