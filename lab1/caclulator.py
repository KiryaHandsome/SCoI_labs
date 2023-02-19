def calculate(a, b, operation):
    if operation == 'div':
        return a / b
    elif operation == 'mul':
        return a * b
    elif operation == 'sub':
        return a - b
    elif operation == 'add':
        return a + b
    else:
        raise Exception('Sorry, this operation is not supported :(')
