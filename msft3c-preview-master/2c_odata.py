import urllib

fin = open('in.txt', 'r')
fout = open('out.txt', 'w')

filters = fin.readlines()
for filter in filters:
	url = 'http://services.odata.org/Northwind/Northwind.svc/Products/$count?$filter=' + urllib.quote(filter.strip())
	print(url)
	fout.write(urllib.urlopen(url).read().decode('utf-8') + '\n')
