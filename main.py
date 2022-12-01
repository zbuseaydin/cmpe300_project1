import random
import time


sizes = [1, 5, 10, 25,  50, 75, 100, 150, 200, 250]
def function(arr):
    arr2=[0] * 5
    n = len(arr)
    
    for i in range(n):
        if(arr[i]==0):
            for t1 in range(i, n):
                p1 = t1 ** 0.5
                x1 = n + 1
                while(x1 >= 1):
                    x1 = x1//2
                    arr2[i%5] += 1
        
        elif (arr[i] == 1):
            for t2 in range(n, 0, -1):
                for p2 in range(1, n+1):
                    x2 = n+1
                    while (x2 > 0):
                        x2 = x2//2
                        arr2[i%5] += 1

        elif (arr[i]==2):
            for t3 in range(1, n+1):
                x3 = t3 + 1
                for p3 in range(0, t3**2):
                    arr2[i%5] += 1

    return arr2

best_times = []
average_times = []
worst_times = []

def average_case_input(size):
    arr = [0] * size
    for i in range(size):
        tmp = random.randint(0,3)
        arr[i] = tmp
    return [arr, average_times]

def best_case_input(size):
    arr= [0] * size
    return [arr, best_times]

def worst_case_input(size):
    arr= [2] * size
    return [arr, worst_times]


def run(input):
    for size in sizes:
        tmp = input(size)
        arr = tmp[0]
        start = time.time()
        arr2 = function(arr)
        time_executed = (time.time()-start)
        tmp[1].append([time_executed, size])

def print_all():
    tmp = f"Case: %s Size: %d Elapsed Time: %f"
    for i in best_times:
        print(tmp%("best", i[1], i[0]))
    for i in average_times:
        print(tmp%("average", i[1], i[0]))
    for i in worst_times:
        print(tmp%("worst", i[1], i[0]))


run(best_case_input)
run(worst_case_input)
run(average_case_input)
print_all()
