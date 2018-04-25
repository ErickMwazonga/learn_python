data = [
	{"partno": "12345", "quantity": 5},
	{"partno": "1234", "quantity": 3}
]

for x in data:
	if x['partno'] == '1234':
		print(x['quantity'])


# List compression representation
print([x['quantity'] for x in data if x['partno'] == '1234'][0])
