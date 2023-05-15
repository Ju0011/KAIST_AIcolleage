import math

def number_to_digit(n):
    return str(n) if n < 10 else ['A', 'B', 'C', 'D', 'E', 'F'][n-10]

def dec_to_any_list(n,radix):
    new_num = []
    while n > 0:
        new_num.insert(0, n % radix)
        n //= radix
    return ''.join([number_to_digit(element) for element in new_num])

def dec_to_any_string(n, radix):
    new_num = ''
    while n > 0:
        new_num = number_to_digit(n % radix) + new_num
        n = n // radix
    return new_num

def main():
    n = int(input('Enter a number: '))
    if n < 0:
        print("Wrong Input!!!")
        return
    radix = int(input('Enter a radix: '))
    if radix < 2 or radix > 16:
        print("Wrong Input!!!")
        return

    print(f'List: {n} is {dec_to_any_list(n, radix)} in base {radix}')
    print(f'String: {n} is {dec_to_any_string(n, radix)} in base {radix}')

main()