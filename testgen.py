inp1=open("sample.txt","r+")
inp2=open("sample1.txt","w")

n = int(inp1.readline())
inp2.write(str(n))
inp2.write('\n')

for i in range(n):

	inp = inp1.readline()
	h, m = map(int,inp.split())
	inp2.write(inp)

	for j in range(m):

		inpp = inp1.readline()
		a, b = map(int,inpp.split())
		inp2.write(str(a-50))
		inp2.write(' ')
		inp2.write(str(b-50))
		inp2.write('\n')