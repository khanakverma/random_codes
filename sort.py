import time
import random

# Bubble Sort 
def bubble(demo_list):
    n = len(demo_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if demo_list[j] > demo_list[j+1]:  
                demo_list[j], demo_list[j+1] = demo_list[j+1], demo_list[j]

# Selection Sort 
def selection(demo_list):
    n = len(demo_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if demo_list[j] < demo_list[min_index]: 
                min_index = j
        demo_list[i], demo_list[min_index] = demo_list[min_index], demo_list[i]

# Insertion Sort 
def insertion(demo_list):
    n = len(demo_list)
    for i in range(1, n):
        key = demo_list[i]
        j = i-1
        while j >= 0 and key < demo_list[j]: 
            demo_list[j + 1] = demo_list[j]
            j -= 1
        demo_list[j + 1] = key

# Time taken by sorting
def measure_time(sorting_method,demo_list):
    start = time.perf_counter()
    sorting_method(demo_list)
    return time.perf_counter() - start

# Random list
size = 100
random_list = []
for i in range(size):
    random_list.append(random.randint(0, 1000))

# Sorting time test
sort_algorithms = {"Bubble Sort": bubble,"Selection Sort": selection,"Insertion Sort": insertion}

for name, sort_func in sort_algorithms.items():
    demo_list_copy = random_list.copy()
    time_taken = measure_time(sort_func, demo_list_copy)
    print(name,"-",time_taken)
