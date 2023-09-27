n = int(input())
count = 0

def get_result(n, case):
    result = 0
    
    if case == 1:
        result += n // 5
        n %= 5

        result += n // 2
    else:
        result += n // 5 - 1
        n %= 5
        n += 5

        result += n // 2

    return result

if n < 5 and n % 2 != 0:
    count = -1
elif (n // 5) % 2 == 0:
    if n % 2 == 0:
        count = get_result(n, 1)
    else:
        count = get_result(n, 2)
else:
    if n % 2 == 0:
        count = get_result(n, 2)
    else:
        count = get_result(n, 1)


print(count)