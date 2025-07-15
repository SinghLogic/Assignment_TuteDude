
a=int(input("Enter a number:"))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result= factorial(a)
print(f"Factorial of {5} is: {result}")