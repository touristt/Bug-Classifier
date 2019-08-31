import numpy as np
from Bug import Bug

training_data = [{'l': 5, 'w': 4, 'T': 1}, {'l': 3, 'w': 1, 'T': 0}, {'l': 5.7, 'w': 4.4, 'T': 1}, {'l': 6.2, 'w': 4, 'T': 0}, {'l': 1, 'w': 16, 'T': 1}, {'l': 18, 'w': 15, 'T': 1}, {'l': 1, 'w': 15, 'T': 1}, {'l': 20, 'w': 14, 'T': 1}, {'l': 16, 'w': 19, 'T': 1}, {'l': 16, 'w': 5, 'T': 0}, {'l': 19, 'w': 17, 'T': 1}, {'l': 7, 'w': 14, 'T': 1}, {'l': 7, 'w': 19, 'T': 1}, {'l': 11, 'w': 9, 'T': 1}, {'l': 2, 'w': 4, 'T': 1}, {'l': 13, 'w': 13, 'T': 1}, {'l': 6, 'w': 19, 'T': 1}, {'l': 16, 'w': 9, 'T': 0}, {'l': 11, 'w': 7, 'T': 0}, {'l': 11, 'w': 20, 'T': 1}, {'l': 16, 'w': 16, 'T': 1}, {'l': 7, 'w': 6, 'T': 1}, {'l': 1, 'w': 11, 'T': 1}, {'l': 14, 'w': 17, 'T': 1}, {'l': 15, 'w': 14, 'T': 1}, {'l': 9, 'w': 11, 'T': 1}, {'l': 13, 'w': 2, 'T': 0}, {'l': 11, 'w': 2, 'T': 0}, {'l': 9, 'w': 5, 'T': 0}, {'l': 15, 'w': 13, 'T': 1}, {'l': 2, 'w': 12, 'T': 1}, {'l': 1, 'w': 19, 'T': 1}, {'l': 11, 'w': 17, 'T': 1}, {'l': 7, 'w': 1, 'T': 0}, {'l': 14, 'w': 6, 'T': 0}, {'l': 15, 'w': 14, 'T': 1}, {'l': 12, 'w': 19, 'T': 1}, {'l': 5, 'w': 3, 'T': 0}, {'l': 8, 'w': 17, 'T': 1}, {'l': 8, 'w': 10, 'T': 1}]

def activation_function(num):
	return 1 if num >= 0 else 0

count = 0
i = 0
while count != len(training_data):
	if i == len(training_data):
		i = 0
	obj = training_data[i]
	inp = np.array([[obj['l'],obj['w']]])
	res = W.dot(inp.transpose()) + B
	res = activation_function(res)
	if res != obj['T']:
		E = obj['T'] - res
		W = W + E*inp
		B = B + E
		count = 1
	else:
		count += 1
	i += 1

def Test(bug):
	inp = np.array([[bug.length, bug.width]])
	res = W.dot(inp.transpose()) + B
	res = activation_function(res)
	if res == 1:
		print("It's a ladybird")
	elif res == 0:
		print("It's a caterpillar")