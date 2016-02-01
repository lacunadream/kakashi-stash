def fact(n):
	if n >= 0:
		n * fact(n)
		n = n-1

# print(fact(4))

a = [3,7,8,11,21,39,40,100,101]
b = [2,3,4,5]

#collate

def collate(listA, listB):
	c = []
	for a in listA: 
		for b in listB: 
			if a < b:
				c.append(a)

	return c



def collate_ans(listA, listB):
	listC = []
	num = len(listA) + len(listB)
	A = 0
	B = 0
	C = 0
	while (A < len(listA) and B < len(listB)):
		if (listA[A] <= listB[B]):
			listC.append(listA[A])
			A = A + 1
		else: 
			listC.append(listB[B])
			B = B + 1

	while (A < len(listA)):
		listC.append(listA[A])
		A = A + 1

	while (B < len(listB)):
		listC.append(listB[B])
		B = B + 1
	return listC

#print(collate_ans(a, b))


def binarysearch(inputlist, value):
	print(inputlist)
	half = len(inputlist)/2
	half = int(half)
	print(len(inputlist))
	print(half)
	flag = 0
	while flag == 0:
		if inputlist[half] == value:
			flag = 1
			print(inputlist[half])
			return half
		elif inputlist[half] > value:
			# to the left
			half = int(half / 2)

		else: 
			half = int((len(inputlist) - half)/2+half)
			print('the current half is %s' %half)

print(binarysearch(a, 101))

print(a[8])
			
## Merge Sort
# use collage?
# need to write split





