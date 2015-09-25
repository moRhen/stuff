try:
	while True:
		print('\n' * 100)
		operation = list(input('Enter a mathematical operation with no space symbol \nAviable operations: +, -, *, / (e.g 2+3)\nTo quit pres CTRL + C\n'))
		first = []
		n=0
		for x in operation:
			if x in ['+', '-', '*', '/']:
				break
			elif x in [str(n) for n in range(10)]:
				first.append(x)
				n+=1

		operation = operation[n:]
		operator = operation[0]
		second = int(''.join(operation[1:]))
		first = int(''.join(first))

		if operator == '+':
			result = first + second
		elif operator == '-':
			result = first - second
		elif operator == '*':
			result = first * second
		elif operator == '/':
			result = first / second

		print('Result for operation: {} {} {} is equal to: {} \n\nPress ENTER to continue, or CTRL + C to quit'.format(first, operator, second, result))
		input()
except KeyboardInterrupt:
	print('\n\nEnd of work :)\n\n')
