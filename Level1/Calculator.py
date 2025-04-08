try:
    num1 = int(input('Enter your first number: '))
    op = input('Enter the operator(+, -, *, /, %): ')
    num2 = int(input('Enter your second number: '))
except ValueError:
    print('Value passed is invalid must be a number')

try:
    match op:
        case "+":
            answer = num1 + num2
            print(f'The answer is {answer}')
        case "-":
            answer = num1 - num2
            print(f'The answer is {answer}')
        case "*":
            answer = num1 * num2
            print(f'The answer is {answer}')
        case "/":
            if num2 == 0:
                print('Cannot divide by 0')
            else:
                answer = num1 / num2
                print(f'The answer is {answer}')
        case "%":
            answer = num1 % num2
            print(f'The answer is {answer}')
        case _:
            print('Operator is invalid')
            
except NameError:
    print('Ensure all fields are filled!')

