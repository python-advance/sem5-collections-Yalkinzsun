## Коллекции

**Инвариантная самостоятельная работа**

4.1. Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка. 

Функция заполнения списка случайными значениями с использованием библиотеки **random**. Функция принимает 2 агрумента: первый - дипазон чисел, из которых будет сгенерирован список, второй - количество элементов, которым должен обладать сгенерированный список

```Python
def get_random_list(x,y):
  import random
  items = list(range(x))
  return random.choices(items, k=y)

new_list = get_random_list(10,5)
```
Сортировка методом вставки:
```python
def insertion_sort(lst):
    for i in range(len(lst)):
        v, j = lst[i], i
        while (lst[j-1] > v) and (j > 0):
            lst[j] = lst[j-1]
            j = j - 1
        lst[j] = v
    return lst
```

Сортировка плавным методом (кучами):

```python
def heapSort1(li):
    def downHeap(li, k, n):
        new_elem = li[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and li[child] < li[child+1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem
    size = len(li)
    for i in range(size//2-1,-1,-1):
        downHeap(li, i, size)
    for i in range(size-1,0,-1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i)
return li
```

Сортировка с помощью встроенных функций языка:
```python
sorted_list = sorted(new_list)
sorted_list1 = sorted(new_list, reverse=True) #сортируем в обратном порядке
```

**Параметрическое тестирование функции insertion_sort с помощью модуля pytest**

В отдельном файле test_main.py:

```Python
import pytest
from main import insertion_sort


@pytest.mark.parametrize("description,unsorted,expected", [
    ("positive", [2, 1, 3, 10], [1, 2, 3, 10]),
    ("negative", [-2, -1, -3, -100], [-100, -3, -2, -1]),
    ("including zero", [2, 0, 1], [0, 1, 2]),
    ("duplicate values", [0, 5, 1, 0, 5], [0, 0, 1, 5, 5]),
    ("floats", [0.1, 0.3, 0.2], [0.1, 0.2, 0.3]),
])
def test_main_sort(description, unsorted, expected):
    assert insertion_sort(unsorted) == expected
```
Запуск теста из консоли: ``>python -m pytest -v test_main.py``

Результат: тест пройден для всех параметров!

![](https://github.com/python-advance/sem5-collections-Yalkinzsun/blob/master/%D0%98%D0%BD%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/1.png)

4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

Для критерия чётность/нечётность функция может выглядеть следующим образом:

```Python
def listenaor(lst):
  lst1, lst2, final_lst = [], [], []
  for i in lst:
      if i % 2 == 1:
          lst1.append(i)
      else:
          lst2.append(i) 
  final_lst.append(lst1)      
  final_lst.append(lst2)
  return final_lst
```

Для критерия "положительные/отрицательные" достаточно поменять условие оператора if:

```Python
  ...
     if i < 0:
         lst1.append(i)
     else:
         lst2.append(i)
  ...
```

**Вариативная самостоятельная работа**

4.3. Создание программы, позволяющей выполнять основные операции (объединение, пересечение, вычитание) над множествами (количество элементов в множестве и их элементы вводятся вручную).

За всё работу отвечат 2 функции. Первая - за ввод множеств и передачу их для второй функции:

```Python
def get_sets():
  a = int(input('Введите количество множеств: '))
  lst = []
  for i in range(a):
     elem = input('Введите множество через запятую: ')
     elem = elem.split(",")
     lst.append(set(elem))
  a = ' 1) Объединение множеств (a | b)\n'
  b = ' 2) Пересечение множеств (a & b)\n'
  c = ' 3) Разность множеств (a - b)\n'
  num = int(input('Доступные операции: \n' + a + b + c + 'Введите номер операции: '))
return lst, num
```

Метод **split()** разбивает получаемую строку на части, используя специальный разделитель - `","`, и возвращает эти части в виде списка, который далее переопределяется в ловарь: `set(elem)`

Основная функция принимает аргументы от первой. В зависимости от выбранной операции происходят объединение, пересечение и разность множеств:
```Python
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
```

Все операции над множетсвами выполняются с помощью 3 методов:
```
.update() - обновление 
.intersection_update() - пересечение
.difference_update() - вычитание
```

Результат выполнения программы:
```Python
Введите количество множеств: 2
Введите множество через запятую: 1, 0, -5, 777
Введите множество через запятую: 16
Доступные операции:
 1) Объединение множеств (a | b)
 2) Пересечение множеств (a & b)
 3) Разность множеств (a - b)
Введите номер операции: 1
Результат: {'1','16','0','-5','777'}
```
