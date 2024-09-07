

def First():
	num = int(input('Введите число: '))

	if num > 0:
		for x in range(1, num+1):
			print(x)
	else:
		for x in range(1, num-1, -1):
			print(x)

def Second():
	num1 = int(input('Введите первое число: '))
	num2 = int(input('Введите второе число: '))
	
	#print('Большее число:', max(num1, num2)) - Самое простое
	
	#Но требуется наверное:
	if num1 > num2:
		print('Большее число:', num1)
	elif num2 > num1:
		print('Большее число:', num2)
	else:
		print('Равные')
	
First()
print()
Second()
