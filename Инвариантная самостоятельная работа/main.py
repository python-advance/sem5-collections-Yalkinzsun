###############
# Задание 4.1 #
###############

def get_random_list(x,y):
  import random
  items = list(range(x))
  return random.choices(items, k=y)

new_list = get_random_list(10,5)
print(new_list)

#метод вставки
def insertion_sort(lst):
    for i in range(len(lst)):
        v, j = lst[i], i
        while (lst[j-1] > v) and (j > 0):
            lst[j] = lst[j-1]
            j = j - 1
        lst[j] = v
    return lst

#print(insertion_sort(new_list))

#метод плавной сортировки 

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

#print(heapSort1(new_list))

#с помощью встроенных функций языка
sorted_list = sorted(new_list)
sorted_list1 = sorted(new_list, reverse=True) #сортируем в обратном порядке
#print(sorted_list1)

###############
# Задание 4.2 #
###############

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

#print(listenaor(new_list))
