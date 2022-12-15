def NumberCheck(var1):
    if var1 % 7 == 0 and var1 % 5 == 0:
        string = 'fizzbuzz'
        return string
    elif var1 % 5 == 0:
        string = 'fizz'
        return string
    elif var1 % 7 == 0:
        string = 'buzz'
        return string
    else:
        string = 'miss'
        return string


NumberCheck(5)
NumberCheck(7)