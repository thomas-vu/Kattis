correct = {'**** ** ** ****': '0',
           '  *  *  *  *  *': '1',
           '***  *****  ***': '2',
           '***  ****  ****': '3',
           '* ** ****  *  *': '4',
           '****  ***  ****': '5',
           '****  **** ****': '6',
           '***  *  *  *  *': '7',
           '**** ***** ****': '8',
           '**** ****  ****': '9'}

line1 = input()
line2 = input()
line3 = input()
line4 = input()
line5 = input()

ans = ''
for i in range((len(line1)+1)//4):
	digit  = line1[i*4:i*4+3]
	digit += line2[i*4:i*4+3]
	digit += line3[i*4:i*4+3]
	digit += line4[i*4:i*4+3]
	digit += line5[i*4:i*4+3]
	if digit in correct:
		ans += correct[digit]
	else:
		print('BOOM!!')
		raise SystemExit

print('BEER!!' if int(ans) % 6 == 0 else 'BOOM!!')
