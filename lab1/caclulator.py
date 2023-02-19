import constants


def calculate(a, b, operation):
    if operation == constants.DIVISION:
        return a / b
    elif operation == constants.MULTIPLICATION:
        return a * b
    elif operation == constants.SUBTRACTION:
        return a - b
    elif operation == constants.ADDITION:
        return a + b
    else:
        raise Exception('Sorry, this operation is not supported :(')
