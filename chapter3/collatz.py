import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True:
    try:
        user_input = int(input())

        result = collatz(user_input)
        print(result)

        if result == 1:
            break

    except ValueError:
        print('Error: Non-integer value provided.')

    except KeyboardInterrupt:
        sys.exit() 