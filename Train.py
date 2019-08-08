from Bug import Bug  #Bug(width,length)

training_data = [Bug(3,1),Bug(1,3)]

slope = 0.25 # Y = mX (m = 0.25)
L = 0.45 	 # Learning Rate

for bug in training_data:
	y = slope * bug.width 
	Y = bug.length
	E = Y - y
	change_in_slope = E / bug.width
	change_in_slope *= L
	slope += change_in_slope
	print(slope)

