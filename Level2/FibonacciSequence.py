def fibonacci_seq(num):
    if num <= 0:
        print('Please enter a positive integer')
    elif num == 1:
        print('Fibonacci sequence is: 0')
    elif num == 2:
        print('Fibonacci sequence is: 0, 1')
    else:
        f_seq = [0, 1]
        for i in range(2, num):
            next_item = f_seq[-2] + f_seq[-1]
            f_seq.append(next_item)
        print(f"Fibonacci sequence is: {', '.join(str(num) for num in f_seq)}")

try:
    user_num = int(input('Enter a positive integer: \n'))
    fibonacci_seq(user_num)

except ValueError:
    print('Please enter a valid input!! (positive integer)')