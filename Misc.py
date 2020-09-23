def removeInRange(list1, value, start, end):
	index = 0
	for i in list1:
		if index >= int(start) and index < int(end):
			if i == int(value):
				list1.remove(i)
		index += 1

	return list1

list1 = [1, 2, 4, 5, 5, 5, 6, 7, 4, 3, 5]

print(removeInRange(list1, 6, 4, 9))

def reverse(dict1):
	invertedDict = dict()
	for k, v in dict1.items():
		invertedDict.setdefault(v, list()).append(k)

	return invertedDict

myDict = {
  'Leo': 1, 
  'Sean': 2, 
  'Lena': 3, 
  'Mara': 4
}

print(reverse(myDict))


