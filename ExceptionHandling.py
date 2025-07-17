x = input('Enter first number:')
y = input('Enter second number:')
try:
    z = float(x) / float(y)
except ZeroDivisionError as e:
    print('Exception Type:ZeroDivisionError')
    z = None
    '''except Exception as e:
        print('Exception Type:',type(e).__name__)
        z = None'''