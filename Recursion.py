# def firstMethod():
#     secondMethod()
#     print("I am the first method.")
# def secondMethod():
#     thirdMethod()
#     print("I am the second method.")
# def thirdMethod():
#     fourthMethod()
#     print("I am the third Method.")
# def fourthMethod():
#     print("I am the fourth Method.")
# #example number two
# def recursiveMethod(n):
#     if n < 1:
#         print("n is less than 1")
#     else:       
#         recursiveMethod(n-1)
#         print(n)


# recursiveMethod(7)

# def factorial(n):
#     assert n >=0 and int(n) == n, "The number must be a positive number only."
#     if n in [0,1]:
#         return 1
#     else:
#         return n * factorial(n-1)
# #the function ends when number is 0 or 1 or a negative number.
# print(factorial(10))

# def fibonacci():
#     n = int(0)
#     while n <= 10:
#         n = n + 1
#     print (n)
#     if n in [0,1]:
#         return n
#     else:
#         return n-1 + n-2    
# print(fibonacci())

# def fibonacci():
#     i = int(0)
#     while i <= 10:
#         i = i + 1
#         print (i)
#     else:
#         return ""
# print(fibonacci())

def fibonacci(n):
    assert n>= 0 and int(n) == n, "Fibonacci number cannot be negative number or non-integer."
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

#wrote my own code where the numbers jut loop through
i = 0
fibonacci = 0
while i <= 10:
    i = i+1
    print(f"I is: {i}")
    fibonacci = (i - 1) + (i - 2) 
    print(f"fibonacci for {i} is: {fibonacci} ")


    