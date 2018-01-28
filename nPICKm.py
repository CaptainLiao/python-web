def factorial(end, start = 1):
    if (start > end or end <= 1):
        return 1
    return end * factorial(end -1, start)

def choose(n,k):
    if n - k < 0:
        return 0
    return factorial(n, k+1) / factorial(n - k)

print choose(1,1), 1
print choose(5,4), 5
print choose(10,5), 252
print choose(10,20), 0
print choose(52,5), 2598960
