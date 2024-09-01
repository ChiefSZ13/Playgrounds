def print_fibo(n):
    current = 1
    previous = 0
    for _ in range(n):
        print(current)
        temp = current
        current += previous
        previous = temp

def fiboEvenSum(n):  #Define a function for fiboEvenSum.
    current = 1   #Create a variable for the current value.
    previous = 1   #Create a variable for the previous value.
    sum = 0    #Create a variable for the even sum.
    while current <= n:    #Loop while fib sequence is smaller than target.
        if current % 2 == 0:
            sum += current    #If current fib is an even number, add to the sum.
        current, previous = current + previous, current   #Calculate the next fib and update the variables.
    return sum    #Return the sum value.

print(fiboEvenSum(4000000))