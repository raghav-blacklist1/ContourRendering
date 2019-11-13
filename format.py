inp1=open("test","r+")
inp2=open("test_formatted","w")

for line in inp1:

	x, y = map(int,line.split(','))
	inp2.write(str(x))
	inp2.write(' ')
	inp2.write(str(y))
	inp2.write('\n')