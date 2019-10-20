d = {'A': '.-',
	 'B': '-...',
	 'C': '-.-.',
	 'D': '-..',
	 'E': '.',
	 'F': '..-.',
	 'G': '--.',
	 'H': '....',
	 'I': '..',
	 'J': '.---',
	 'K': '-.-',
	 'L': '.-..',
	 'M': '--',
	 'N': '-.',
	 'O': '---',
	 'P': '.--.',
	 'Q': '--.-',
	 'R': '.-.',
	 'S': '...',
	 'T': '-',
	 'U': '..-',
	 'V': '...-',
	 'W': '.--',
	 'X': '-..-',
	 'Y': '-.--',
	 'Z': '--..',
	 '_': '..--',
	 ',': '.-.-',
	 '.': '---.',
	 '?': '----'}
D = {'.-'  : 'A',
	 '-...': 'B',
	 '-.-.': 'C',
	 '-..' : 'D',
	 '.'   : 'E',
	 '..-.': 'F',
	 '--.' : 'G',
	 '....': 'H',
	 '..'  : 'I',
	 '.---': 'J',
	 '-.-' : 'K',
	 '.-..': 'L',
	 '--'  : 'M',
	 '-.'  : 'N',
	 '---' : 'O',
	 '.--.': 'P',
	 '--.-': 'Q',
	 '.-.' : 'R',
	 '...' : 'S',
	 '-'   : 'T',
	 '..-' : 'U',
	 '...-': 'V',
	 '.--' : 'W',
	 '-..-': 'X',
	 '-.--': 'Y',
	 '--..': 'Z',
	 '..--': '_',
	 '.-.-': ',',
	 '---.': '.',
	 '----': '?'}
try:
	while True:
		msg = input()
		morse = ''
		lengths = ''
		for c in msg:
			morse += d[c]
			lengths += str(len(d[c]))
		ans = ''
		i = 0
		for l in map(int, reversed(lengths)):
			ans += D[morse[i:i+l]]
			i += l
		print(ans)
except:
	pass
