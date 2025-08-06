#Multiplication Table

user_number=int(input('Enter a number to do the multiplication table:'))

for multiplication_number in range (0, 11):
	multiplication_table = user_number * multiplication_number
	print(f'{user_number} x {multiplication_number} = {multiplication_table}')