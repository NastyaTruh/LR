
def greet(name):
	print('Привет {}!'.format(name))
	
def square(number):
	return number**2

def max_of_two(x,y):
	#return max(x,y) - Самое простое
	
	#Но судя по всему требовалось:
	if x > y:
		return x
	else:
		return y

def describe_person(name, age=30):
	print('Имя: {}, возраст: {}'.format(name, age))
		
def get_divs(x):
	divs = set()
	for d in range(2, int(x**0.5)+1):
		if x % d == 0:
			divs.add(d)
			divs.add(x//d)
	return divs		
		
def is_prime(number):
	divs = get_divs(number)
	
	return divs == set()

greet('Smb')
print(square(10))
print(max_of_two(2,3))
print()

describe_person('Smb')
print(is_prime(13))
