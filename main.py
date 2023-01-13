def triple(func):
    def wrapper(*args):
        for i in range(1,4):
            print(i, ': ', func(*args), sep='')
    return wrapper


@triple
def squareSum(*args):
    sum = 0
    args = list(args)
    for i in range(len(args)):
        if str(type(args[i])) != "<class 'int'>" and str(type(args[i])) != "<class 'float'>":
            num = args[i]
            index = args.index(num)
            args.pop(index)
            try:
                args.insert(index, int(num))
            except:
                raise TypeError
    for i in range(len(args)):
        sum += args[i] ** 2
    return sum

squareSum(1,'15', 'yeah')