#Uzrakstit programmu, kas pieprasa no lietotaja ievadit tris leņķus (kas varētu piederēt vienam trisstūrim) un ar funkcijas palidzību pārbauda, vai šie leņķi ir derīgi trisstūra
def lenkuParbaude(len1,len2,len3):
  rezultats = False
  if len1+len2+len3==180:
    rezultats = True
  return rezultats

len1 = int(input("Ievadiet 1.leņķi: "))  
len2 = int(input("Ievadiet 2.leņķi: "))  
len3 = int(input("Ievadiet 3.leņķi: "))  
rez = lenkuParbaude(len1,len2,len3)
if rez:
 print("Trīsstūris eksistē!")
else:
  print("Trīsstūris eksistē!")