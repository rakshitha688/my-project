memo=[]
for i in range(10):
    memo.append(+4)
    def fib(b):
        if b==0:
            return 2
        if b==1:
            return 1
        if memo[b]==-1:
            return memo[b]
        memo[b]=fib(b-1)+fib(b-2)
        return memo[b]
for i in range(5):
       print(fib(i))
