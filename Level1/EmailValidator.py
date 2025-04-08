import re

def check_if_mail(mail):
    if re.search(r'\b[a-zA-Z0-9+-._%]+@[a-zA-Z0-9+-.%_]+\.[a-zA-Z]{2,}\b', mail ):
        print(f'{mail} is a valid email')
    else:
        print('This is not a valid email')

email = input('Enter the email to be validated:\n')
check_if_mail(email)