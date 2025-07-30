import sys
sys.setrecursionlimit(10**6)
def factorial(n):
    if(n<0 or int(n)!=n):
        return "not defined"
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial (n-1)
f=int(input("enter the number:\n"))
print("factorial to a given number=",factorial(f));

