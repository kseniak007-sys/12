from random import *
n = int(input("Введите длину ДНК цепи: "))
dnk = ""
for i in range(n):
    dnk += choice("ATGC")
dnk1 = dnk
irnk = dnk.replace("A", "U").replace("T", "A").replace("G", "*").replace("C", "G").replace("*", "C")
print(f"Цепь днк: {dnk}")
print(f"Цепь ирнк: {irnk}")
print(f"% содержание аденина: {dnk1.count('A')/len(dnk)*100:.1f}%")
print(f"% содержание тимина: {dnk1.count('T')/len(dnk)*100:.1f}%")
print(f"% содержание гуанина: {dnk1.count('G')/len(dnk)*100:.1f}%")
print(f"% содержание цитозина: {dnk1.count('C')/len(dnk)*100:.1f}%")
