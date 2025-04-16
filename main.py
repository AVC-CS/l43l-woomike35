def main():
    total = 0
    numbers = [0] * 5
    i = 0

    while i < len(numbers):
        numbers[i] = int(input('Enter a value: '))
        i += 1

    total = sum(numbers)
    print(total)

    # Do not delete the return statement
    return total, numbers


if __name__ == '__main__':
    main()
