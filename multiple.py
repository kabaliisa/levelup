def multiple():
    numbers = range(2000, 3201)

    num = []
    for number in numbers:
        if number % 7 == 0 and number % 5 != 0:
            num.append(number)

    return num


print(multiple())
