# 1. Buatlah sebuah program yang menerima inputan sebuah bilangan bulat kemudian mengembalikan nilai faktorial dari bilangan tersebut menggunakan recursive function.


def faktorial(angka, total):
  if angka == 0:
    return
  
  total = total * angka
  
  faktorial(angka-1, total)
  print(total)
  
faktorial(8,1)
