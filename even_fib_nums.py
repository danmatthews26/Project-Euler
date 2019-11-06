fib_numbers = [1,2]
even_fib_nums = []

a = 1
b = 2
while b <= 4000000:
    c = a + b
    a = b 
    b = c
    fib_numbers.append(c)
    
for x in fib_numbers:
    if x % 2 == 0:
        even_fib_nums.append(x)   


c = 0
for x in even_fib_nums:
    c += x

print(c)