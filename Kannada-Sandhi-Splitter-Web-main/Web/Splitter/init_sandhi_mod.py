#Author Akshatha Arodi 
#dtd 10/03/2015 as a part of my major project kannada spell checker with sandhi splitter 

import dawg
from sys import argv
from array import *
#import spell_check_mod1
from Splitter.spell_check_mod1 import *
#holder for the dictionary

'''
dictWords=[]
f = open("Splitter/Dictionaries/wx_dictionary2.txt", "r")

#read and append words to dictWords
p = 0
for line in f:
	if(p<10):
		print(f"Line : {line}")
	dictWords.append(line.strip())
	p+=1

#creating a dawg data structure
#dict_dawg = dawg.CompletionDAWG(dictWords)
for word in dictWords:
	if "maha" in word:
		print(f"Word : {word}")
'''
#sandhi possible places
sandhi_places=['A','aa','uu','ii','ee','oo','ai','au','ya','yu','yo','ye','va','vu','vo','ve', 'RR', 'aR','gi','Dr','hc','jj','cc','sh','Sh','DD','Nm','nG','nm','Hk','Hp','ga','ne','iy','ev','Mc',
'ra','Da','da','bd','gd','ja','du','db','bj','ba','tk','ks','aj','mm','ar','dg','cC','Rr','hv','ls','lv','ys','dy','kc','kt','kp','nu','rv','TT','iv','Nc','av','Mj','Nj','Tm','Ca','nn','kR','dr','ll',
'Hr','ir','ur','gv']

#for aagama and aadeesha
kannada_sandhi_places=['g','b','d','y','v']

lopa_places=['a','e','i','o','u']

prefix_vowels=['a','i','u','R']

suffix_vowels1=['aa','ii','uu','RR','ee','ai','oo','au']
suffix_vowels2=['a','i','u','R','e']
