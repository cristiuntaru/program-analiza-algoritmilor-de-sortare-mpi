import random
import time

def main():
    size = int(input("Introduceți dimensiunea listei: "))
    
    list_types = {
        "Random": [random.randint(-100, 1000000) for _ in range(size)],
        "Sorted": list(range(size)),
        "Reversed": list(range(size, 0, -1)),
        "Identical": [7] * size
    }
    
    print("\nTipuri de liste disponibile:")
    for key in list_types:
        print(f"- {key}")
    list_choice = input("Alegeți tipul de listă pe care doriți să o sortați: ")
    lista = list_types[list_choice]

    sorting_algorithms = {
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Bubble Sort": bubble_sort,
        "Quick Sort": quicksort,
        "Merge Sort": mergeSort,
        "Counting Sort": lambda lista, max_val=100100: counting_sort(lista, max_val) 
    }

    
    print("\nAlgoritmi de sortare disponibili:")
    for key in sorting_algorithms:
        print(f"- {key}")
    algo_choice = input("Alegeți algoritmul de sortare: ")

    print("\nLista înainte de sortare:")
    print(lista)

    start_time = time.time()
    if algo_choice == "Counting Sort":
        max_val = max(lista) + 1 if lista else 0 
        sorted_list = sorting_algorithms[algo_choice](lista, max_val)
    else:
        sorted_list = sorting_algorithms[algo_choice](lista)
    end_time = time.time()


    print("\nLista după sortare:")
    print(sorted_list)
    print(f"Timpul necesar sortării: {end_time - start_time:.3f} secunde")





# Functiile de sortare


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista



def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista



def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista




def quicksort(lista):
    stack = [(0, len(lista) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot = lista[start]
        left = start + 1
        right = end
        while left <= right:
            while left <= end and lista[left] <= pivot:
                left += 1
            while right > start and lista[right] > pivot:
                right -= 1
            if left < right:
                lista[left], lista[right] = lista[right], lista[left]
        lista[start], lista[right] = lista[right], lista[start]
        stack.append((start, right - 1))
        stack.append((right + 1, end))
    return lista



def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
        return lista
    



def counting_sort(lista, max_val):
    counts = [0] * (max_val + 1)
    for val in lista:
        counts[val] += 1
    sorted_lista = []
    for i in range(max_val + 1):
        sorted_lista += [i] * counts[i]
    return sorted_lista




# Rularea programului principal
if __name__ == "__main__":
    main()
    
