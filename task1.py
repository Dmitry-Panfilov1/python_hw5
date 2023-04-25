a = int(input('enter A: '))
b = int(input('enter B: '))
def power(n1, n2):
    if n2 == 0:
        return 1
    elif n2 == 1:
        return n1
    else:
        return n1 * power(n1, n2 - 1)
print(power(a, b))