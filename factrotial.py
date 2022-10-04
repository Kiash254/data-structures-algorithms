#fuctorial work using python


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
value=int(input("Enter a number to find its factorial: "))
print("The factorial of",value,"is",factorial(value))