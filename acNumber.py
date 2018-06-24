def ACNumber(n):
    number = str(n)
    result = 0
    for i in range(len(number)):
        integer = int(number[i])
        result += integer**len(number)
    if result == n:
        return True
    else:
        return False
print(ACNumber(154))
print(ACNumber(153))
