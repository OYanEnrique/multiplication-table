# Multiplication Table v1.1.0
print('=-' * 15)
print('Infinite Multiplication Table')
print('=-' * 15)

while True:
	number = int(input('Enter a non negative number:'))
	print('=' * 30)
	if number <0:
		print('Program closed successfully')
		break
	for y in range(1,11):
		print(f'{number} x {y} = {number*y}')
	print('='*30)
