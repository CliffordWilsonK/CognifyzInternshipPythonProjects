def temperature_conversion(value, unit):
        if unit.lower() == 'c' or unit.lower() == 'celsius':
            answer = (value * (9/5)) + 32
            return f'Converted value is {answer:.1f} °F'
        elif unit.lower() == 'f' or unit.lower() == 'fahrenheit':
            answer = (value - 32) * (5/9)
            return f'Converted value is {answer:.1f} °C'
        else:
            return 'Unit is invalid!'
        
try:
    value = int(input('Enter the temperature value:\n'))
    unit = input('Enter the temperature unit(C or Celsius| F or Fahrenheit ):\n')

except ValueError:
        print('Enter the right value')


answer = temperature_conversion(value, unit)
print(answer)