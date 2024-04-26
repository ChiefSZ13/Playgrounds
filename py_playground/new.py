def print_fibo(n):
    current = 1
    previous = 0
    for _ in range(n):
        print(current)
        temp = current
        current += previous
        previous = temp

def fiboEvenSum(n):
    current = 1
    previous = 1
    sum = 0
    while current <= n:
        if current % 2 == 0:
            sum += current
        current, previous = current + previous, current
    return sum

print(fiboEvenSum(4000000))