def topla(n):
    if n==1:
        return 1
    if n<=0:
        return "0'dan büyük olmalı"
    else:
        return n+topla(n-1)



a=int(input("Bir sayı giriniz:"))
print(f"1 den {a}'ye kadar olan sayıların toplamı  = {topla(a)}")
      
