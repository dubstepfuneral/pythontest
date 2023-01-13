def triple(func):
    def wrapper(*args, amount=0):
        for i in range(1,4):
            print(i, ': ', func(*args, amount=amount), sep='')
    return wrapper


@triple
def squareSum(*args, amount=0):
    sum = 0
    for i in range(amount):
        sum += args[i] ** 2
    return sum

squareSum(1,2,3,4,amount=4)