def check_if_palindrome(string):
    reversed_str = string[::-1]
    if string.lower() == reversed_str.lower():
        print(f'{string} is a palindrome')
    else:
        print(f'{string} is not a palindrome')

word_to_check = 'Madam'

check_if_palindrome(word_to_check)