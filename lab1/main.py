from even_numbers import generate_numbers
from even_numbers import evens
from hello_world import say_hello
from caclulator import calculate


if __name__ == '__main__':
    say_hello()
    print(calculate(12, 14, 'div'))
    numbers = generate_numbers()
    print(evens(numbers))
