def main():
    total = 0
    i = 0

    while i < 5:
        num = int(input(f"Enter number {i + 1}: "))
        total += num
        i += 1

    print("The total is:", total)

    return total


if __name__ == '__main__':
    main()
