def fibonacci(n):
    if n<=0:
        return "yok"
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return int(fibonacci(n-1)) + int(fibonacci(n-2))



for i in range(1,31):
     print(fibonacci(i),end =" ")                   
