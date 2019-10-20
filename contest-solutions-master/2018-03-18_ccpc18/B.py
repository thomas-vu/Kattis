def gcd(a, b):
	if not b:
		return a
	return gcd(b, a % b)

a, b = map(int, input().split('/'))
a -= 32 * b
a *= 5
b *= 9

g = gcd(a, b)
print('{}/{}'.format(a // g, b // g))