#okay, rethink this logic
# for i in n(range(0,10)):
#      fibonacci(n-1) + fibonacci(n-2)
'''
     THE CODE THAT WORKED!
'''
i = 0
fibonacci = 0
while i <= 10:
    i = i+1
    print(f"I is: {i}")
    fibonacci = (i - 1) + (i - 2) 
    print(f"fibonacci for {i} is: {fibonacci} ")
