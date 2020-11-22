# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def dividors(n, k = 2):
  if n == 1:
    return
  elif n % k == 0:
    print(k)
    dividors(n // k, k)
  else:
    dividors(n, k + 1)


def dividors_tail(n, k = 2):
  while n > 1:
    if n % k == 0:
      print(k)
      n = n // k
    else:
      k = k + 1
