import math

def is_prime(n):    
    if n <= 1:    
       return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):    
        if n % i == 0:    
            return False   
    return True  

def get_prime_num(n):
    return [i for i in range(1, n + 1) if is_prime(i)]

def count_specMult(n, maxVal):
    num = 1
    prime_num = get_prime_num(maxVal)[:n]
    raw_val = reduce(lambda x, y: x * y, prime_num)
    while raw_val * (num + 1) < maxVal:
        num = num + 1
    return num

print count_specMult(4, 500)




def pascal(p):
    m = []
    def digui(n):
        res = []
    
        if p == 1:
            return [1]
        else:
            arr = pascal(p -1)
            m.appen(arr)
            res = [arr[i] + arr[i+1] for i in range(len(arr) - 1)]
            res.insert(0, 1)
            res.insert(len(res), 1)
            return res
        
        

