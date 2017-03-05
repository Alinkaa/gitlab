import re
hand = open(raw_input('Enter file name: '),'r') 
numlist = [] 
for line in hand: 
    line = line.rstrip() 
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) 
    if len(stuff) != 1: continue
    num = float(stuff[0]) 
    numlist.append(num) 
print "Maximum: " + str(max(numlist))

if __name__ == '__main__': 
test1 = findSumReg("321.txt") 
assert '44' == str(test1)[:2] and '22' == str(test1)[-2☺ 
print "1. Amount of test 1 is: " + str(test1)
