def char_replace(word):
	word = word.replace('A','aa')
	word = word.replace('I','ii')
	word = word.replace('U','uu')
	word = word.replace('W','th')
	word = word.replace('T','Th')
	word = word.replace('D','Dh')
	chars = [i for i in word]
	for i in range(len(chars)-1):
		if chars[i]=='o' and chars[i+1]=='V':
			chars[i+1]=''
		elif chars[i]=='o' and chars[i+1]!='V':
			chars[i]='oo'
		elif chars[i]=='e' and chars[i+1]=='V':
			chars[i+1]=''
		elif chars[i]=='e' and chars[i+1]!='V':
			chars[i]='ee'
	if chars[-1]=='o':
		chars.append('o')
	elif chars[-1] == 'e':
		chars.append('e')
	for i in range(len(chars)-1):
		if chars[i]=='t' and chars[i+1]!='h':
			chars[i]='T'
			
	if chars[-1] == 't':
		chars[-1] = 'T'
	elif chars[-1] == 'w':
		chars[-1]='t'
	elif chars[-1] == 'd':
		chars[-1] = 'D'
	word = ''.join(chars)
	
	word = word.replace('E','ai')
	word = word.replace('O','au')
	word = word.replace('d','D')
	word = word.replace('S','sh')
	word = word.replace('R','Sh')
	word = word.replace('f','nG')
	word = word.replace('P','ph')
	word = word.replace('X','dh')
	word = word.replace('x','d')
	word = word.replace('w','t')
	word = word.replace('B','bh')
	word = word.replace('q','R')
	word = word.replace("lY","L")
	word = word.replace("G","gh")
	word = word.replace('K','kh')
	word = word.replace('C','ch')
	word = word.replace('J','jh')
	
	return word
	
