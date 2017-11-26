# Copyright 2017 Keval Khara kevalk@bu.edu

f=open("p022_names.txt",'r')

# Making a dictionary for storing scores of each alphabet
char_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,
"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,
"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

# Making a list of words from the text file
names=sorted(f.read().replace('"','').split(','))

sum=0
for ind,val in enumerate(names):
	temp=0
	for x in val:
		temp+=char_dict[x]
	sum+=temp*(ind+1)
	
print(sum)
