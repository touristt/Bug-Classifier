import numpy as np
from Bug import Bug
from training_data import training_data
from test_data import test_data
def activation_function(num):
	return 1 if num >= 0 else 0

W = np.array([[0 , 0]]) # initial weights
B = 0 			# initial bias

count = 0
i = 0
iterations = 0
print("Training Data Length:",len(training_data))
print("Test Data Length:",len(test_data)) 
while count != len(training_data):
	iterations+=1
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
print("Iterations:",iterations,", Weights:",W,", Bias:",B)

def Test():
	count = 0
	for bug in test_data:
		inp = np.array([[bug['l'], bug['w']]])
		res = W.dot(inp.transpose()) + B
		res = activation_function(res)
		if res == bug['T']:
			count += 1
	print("Accuracy: ", count*100/len(test_data), "%")

# Custom Tests:
def Check(bug):
	inp = np.array([[bug.length, bug.width]])
	res = W.dot(inp.transpose()) + B
	res = activation_function(res)
	if res == 1:
		print(f"L: {bug.length}, W: {bug.width} It's a ladybird")
	elif res == 0:
		print(f"L: {bug.length}, W: {bug.width} It's a caterpillar")
Test()
Check(Bug(4,5))
Check(Bug(1,3))
Check(Bug(3,1))
Check(Bug(16,5))
Check(Bug(31,23))
Check(Bug(4.4,5.7))
Check(Bug(4,6.2))
