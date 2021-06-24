#Recursion
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

powerOfTwo(6)
'''
Recursion isn't advisable for space & time efficient systems.
It is useful for tree traversion (preorder tree traversing more especially) and quick working solutions instead of efficient ones.
It is useful in memoization.
It can be slow.
'''

#iteration
def powerOfTwoIt(n):
    i = 0
    power = i
    while i < n:
        power = power * 2
        i = i + 1
    return power

powerOfTwoIt(6)