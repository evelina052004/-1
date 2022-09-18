while True:
    fib = lambda n: 0if n<1else 1 if n==1 else fib(n-1)+fib(n-2)
    x=int(input("Введите число: "))
    n=0
    while x>fib(n):n+=1
    if fib(n)==x:print("Число Фибоначчи")
    else: print("Не число Фибоначчи")