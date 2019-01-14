opp = {
	'N' : 'S',
	'E' : 'W',
	'S' : 'N',
	'W' : 'E'
}

def dirReduc(data):
	response = []
	for i, v in enumerate(data):
		if opp[v] == response[-1] if len(response) > 0 else 0:
			response.pop()
		else:
			response.append(v)
	return response

needle1 = ['N', 'S', 'S', 'E', 'W', 'N', 'W']
needle2 = ['N', 'S', 'S', 'E', 'W', 'N']
print(dirReduc(needle1))
print(dirReduc(needle2))