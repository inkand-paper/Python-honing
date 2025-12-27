number = float(input("Enter your number: "))


def even_odd(num):
    if (num % 2) == 0:
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number")

def check_multiples(num):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is a multiple of both 3 and 5.")
    elif num % 3 == 0:
        print(f"{num} is a multiple of 3.")
    elif num % 5 == 0:
        print(f"{num} is a multiple of 5.")
    else:
        print(f"{num} is not a multiple of 3 or 5.")

even_odd(number)
check_multiples(number)
