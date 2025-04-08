import re

def password_strength_check(pwd):
    if re.search(r'\s', pwd):
        print('There must be no whitespaces in your password')
    elif len(pwd) >= 8 and re.search(r'[A-D]', pwd) and re.search(r'[0-9]', pwd) and re.search(r'[!@#$%^&*]', pwd) and re.search(r'[a-d]', pwd):
        print('Password is ok✅')
    elif len(pwd) >= 8 and re.search(r'[A-D]', pwd) and re.search(r'[0-9]', pwd) and re.search(r'[a-d]', pwd):
        print('❌Password must contain special characters(!@#$%^&*)')
    elif len(pwd) >= 8 and re.search(r'[A-D]', pwd) and re.search(r'[!@#$%^&*]', pwd) and re.search(r'[a-d]', pwd):
        print('❌Password must contain digits')
    elif len(pwd) >= 8 and re.search(r'[0-9]', pwd) and re.search(r'[!@#$%^&*]', pwd) and re.search(r'[a-d]', pwd):
        print('❌Password must contain uppercase letters')
    elif re.search(r'[0-9]', pwd) and re.search(r'[!@#$%^&*]', pwd) and re.search(r'[a-d]', pwd):
        print('❌Password is too short')
    else:
        print('Password is too weak❌')


password_strength_check('clifford@2')