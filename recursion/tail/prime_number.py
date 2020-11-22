# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

 
def is_prime(n, k = 2):
  if k > n**0.5:
    return ("YES")
  elif n % k == 0:
    return("NO")
  else:
    return is_prime(n, k + 1)

def is_prime_tail(n, k = 2):
  if k > n**0.5:
    return ("YES")
  elif n % k == 0:
    return("NO") 
  k = k + 1
  return is_prime(n, k)




  