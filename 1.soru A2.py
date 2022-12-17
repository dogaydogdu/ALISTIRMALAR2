import random

k=0
while k==0:
    n=str(random.randint(11,99))
    if str(n)[0]!= str(n)[1]:
        k=1


t=1
while t==1:
    i=input("İki basamaklı bir sayı giriniz:")
    if int(i) <= 10 or int(i)>=100:
        print("İki basamaklı girmelisiniz")
        continue
    if i[0]==i[1]:
        print("Rakamlar farklı olmalı")
        continue
    if i[0] == n[0] and i[1] != n[1]:
        print("1")
    if i[0] != n[0] and i[1] == n[1]:
        print("1")
    if i[0] == n[1] and i[1] != n[0]:
        print("-1")
    if i[0] != n[1] and i[1] == n[0]:
        print("-1")
    if i[0] == n[1] and i[1] == n[0]:
        print("-2")
    if i[0] != n[0] and i[0] != n[1] and i[1] != n[1] and i[1] != n[0]:
        print(0)
    if i[0] == n[0] and i[1] == n[1]:
        print("TEBRİKLER ! OYUNU KAZANDINIZ !")
        break
        t=1
    
    
