#пример генератора множетсва a = {i ** 2 for i in range(10)}

def set_operations(lst, operation):
  final_set = set()
  if operation == 1:
     for i in lst:
       final_set.update(i)
  elif operation == 2:
     c = 0
     for i in lst:
       if c == 0:
          final_set.update(lst[0])
          c+=1
       else:
         final_set.intersection_update(i)
  elif operation == 3:
     c = 0
     for i in lst:
       if c == 0:
          final_set.update(lst[0])
          c+=1
       else:
         final_set.difference_update(i)
  return final_set
 
def get_sets():
  a = int(input('Введите колличество множеств:'))
  lst = []
  for i in range(a):
     elem = set(input('Введите множество через запятую и без пробелов: '))
     elem.remove(',')
     lst.append(elem)
  a = ' 1) Объединение множеств (a | b)\n'
  b = ' 2) Пересечение множеств (a & b)\n'
  c = ' 3) Разность множеств (a - b)\n'
  num = int(input('Доступные операции: \n' + a + b + c + 'Введите номер операции: '))
  return lst, num

if __name__ == "__main__":
  x, y = get_sets()
  print('Результат: ', set_operations(x, y))
  
