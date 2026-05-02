jumlah = int(input('Masukkan jumlah elemen: '))

elemen = []
for i in range(jumlah):
  nilai = int(input('Masukkan elemen elemennya:'))
  elemen.append(nilai)

def insertion(data):
    n = len(data)
    for i in range(1, n):
        current_value = data[i]
        j = i - 1
        while j >= 0 and data[j] > current_value:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current_value
    return data

def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)


def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

data_copy = elemen[:]

sort1 = insertion(data_copy)
print(sort1)

quicksort(data_copy)
print(data_copy)

sort3 = countingSort(data_copy)
print(sort3)