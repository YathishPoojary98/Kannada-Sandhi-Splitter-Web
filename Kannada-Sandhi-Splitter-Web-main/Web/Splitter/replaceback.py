def replaceback(word):
	word = word.replace('aa','A')
	word = word.replace('ii','I')
	word = word.replace('uu','U')
	word = word.replace('dh','X')
	word = word.replace('d','x')
	chars = [i for i in word]
	for i in range(len(chars)-1):
		if chars[i]=='o' and chars[i+1]=='o':
			chars[i+1]=''
		elif chars[i]=='o' and chars[i+1]!='o':
			chars[i]='oV'
		if chars[i]=='e' and chars[i+1]=='e':
			chars[i+1]=''
		elif chars[i]=='e' and chars[i+1]!='e':
			chars[i]='eV'
		elif chars[i] == 't' and chars[i+1] != 'h':
			chars[i] = 'w'
		elif chars[i] == 'T' and chars[i+1] != 'h':
			chars[i] = 't'
		elif chars[i] == 'D' and chars[i+1] != 'h':
			chars[i] = 'd'
		
	if len(chars)>=2:
		if chars[-1]=='o' and chars[-2] =='o':
			chars[-1]=''
		elif chars[-1]=='o' and chars[-2]!='o':
			chars.append('V')
		if chars[-1]=='e' and chars[-2] =='e':
			chars[-1]=''
		elif chars[-1]=='e' and chars[-2]!='e':
			chars.append('V')
		elif chars[-1] == 't':
			chars[-1] = 'w'
		elif chars[-1] == 'T':
			chars[-1]='t'
		elif chars[-1] == 'D':
			chars[-1] = 'd'
		
		word = ''.join(chars)
		word = word.replace('ai','E')
		word = word.replace('au','O')
		word = word.replace('th','W')
		
		
		
		word = word.replace('Th','T')
		word = word.replace('Dh','D')
		word = word.replace('sh','S')
		word = word.replace('R','q')
		word = word.replace('Sh','R')
		word = word.replace('nG','f')
		word = word.replace('ph','P')
		word = word.replace('bh','B')
		word = word.replace("L","lY")
		word = word.replace("gh","G")
		word = word.replace('kh','K')
		word = word.replace('ch','C')
		word = word.replace('jh','J')
		
	return word
