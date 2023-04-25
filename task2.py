a = int(input('enter A: '))
b = int(input('enter B: '))
def sum(n1, n2):
    while n2 > 0:
        return sum(n1 + 1, n2 - 1)
    return n1
print(sum(a, b))