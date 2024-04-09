

'''
Use this file for basic input and output.
Do not execute this file. Import this as any other python module. Call the appropriate methods for related jobs.

Syntax:
import ipop

Keep this file in the same directory as the main executable.
'''

from ast import literal_eval

# getUserData(data_types, request_message = '', error_message = None, retry = True, validation = None, quittable = True) -> returns a variable
'''
This function is an alternative to the native input() method.
It combines the features of try, except in case of invalid data, and also a validation expression.

data_types []	:		allowed type of data requested from the user 	{list of data types: int|float|bool|str}
request_message {str}:		(optional) message shown to user before input
error_message {str}:		(optional) error message to be shown to user in case of invalid data type entered
retry {bool}:			(optional) keep trying until a valid data is entered		{True|False}
validation []:			(optional) additional expression (written with respect to variable 'x') to be evaluated for valid data. Write in same prder of data_types[]
quittable {bool}:		(optional) show an option to cancel the input or abort the program		{True|False}

	Example 1: we want to get a float data

		import ipop
		my_float_data = ipop.getUserData([float], "Enter a floating data", "Wrong data entered!")

	Example 2: we want to get an integer greater than 25

		import ipop
		my_int_data = ipop.getUserData([int], "enter an int greater than 25", "wrong data", True, ['x > 25'] )

	Example 3: we want to get an int or float, if integer is entered, it should be less than 5

		import ipop
		my_data = ipop.getUserData([float, int], "enter an integer less than 5 or a float", "wrong input", True, ['True', 'x < 5'])

	*** note that since float is the first of 'data_types', and any float can be accepted, the first 'validation' is 'True'.
	*** similarly we give the validation expression of integer data type as it is next to float in 'data_types'

	Example 4: we want to get any integer OR a float greater than 100 OR a string starting with 'hello'

		import ipop
		my_data = ipop.getUserData([str, float, int], "enter data", "wrong data", True, ['x.startswith("hello")', 'x > 100', 'True'])

'''
def getUserData(data_types, request_message = '', error_message = None, retry = True, validation = None, quittable = True):
	r = True
	invalid_flag = 1
	try:
		t = data_types[0]
	except:
		print ("Please enter a data_type in square braces! example: [int]")
		return None

	while r and invalid_flag == 1:

		r = retry

		print (request_message)
		if quittable:
			print ("Enter '!q' to cancel input, '!!q' to abort program")

		x = input()

		if quittable:
			if x == '!q':
				print ("Input cancelled\n")
				break
			elif x == '!!q':
				print ("Program aborted!\n")
				exit()

		if x != '':
			try:
				x = literal_eval(x)
			except:
				pass
			

			for i in range(len(data_types)):
				dt = data_types[i]
				if type(x) == dt:
					try:
						op = validation[i]
					except:
						invalid_flag = 0
						break
					try:
						if eval(op):
							invalid_flag = 0
							break
					except:
						print ("Validation error. Please properly check the input expression.\n")
						return None

		if invalid_flag == 1:
			if error_message != None:
				print(error_message)

	if invalid_flag == 0:
		return x
	else:
		return None
