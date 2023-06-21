# 
# 

with open(r'./test02.txt', 'r') as f:
	Char3 = f.read(3)
	position = f.tell()

	while Char3:
		print(Char3)
		print(position)

		Char3 = f.read(3)
		position = f.tell()
