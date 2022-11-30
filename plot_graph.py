import random
import time
import matplotlib.pyplot as plt
import math


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
        tmp[1].append([time_executed*2e7, size])
    print(tmp[1])

def print_all():
    tmp = f"Case: %s Size: %d Elapsed Time: %f"
    for i in best_times:
        print(tmp%("best", i[1], i[0]))
    for i in average_times:
        print(tmp%("average", i[1], i[0]))
    for i in worst_times:
        print(tmp%("worst", i[1], i[0]))

        

def plot_best():
    best1= []
    best2 = []
    best3 = []
    best4 = []
    best5 = []
    real = []

    for i in range(10):
        real.append(best_times[i][0]) 
    for i in sizes:
        b2 = math.log2(i)*i*(i+1)/2
        best1.append(i)
        best2.append(b2)
        best3.append(0)
        best4.append(0)
        best5.append(0)

    plt.plot(sizes, real,  'deeppink', label ="real exec")
    plt.plot(sizes, best1, "teal", label =" best1"  )
    plt.plot(sizes, best2, "firebrick",label =" best2")
    plt.plot(sizes, best3, 'blueviolet', label =" best3" )
    plt.plot(sizes, best4, 'blueviolet' , label =" best4")
    plt.plot(sizes, best5, 'blueviolet' , label =" best5")
    

    #plt.xlabel('input size (n)')
    #plt.xticks(sizes)
    plt.legend()
    plt.show()

def plot_worst():
    worst1= []
    worst2 = []
    worst3 = []
    worst4 = []
    worst5 = []
    real = []

    for i in range(10):
        real.append(worst_times[i][0]) 
    for i in sizes:
        w1 = i
        w2 = math.log2(i)*i*(i+1)/2
        worst2.append()
        worst1.append()
        worst3.append(0)
        worst4.append(0)
        worst5.append(0)

    plt.plot(sizes, real,  'deeppink', label ="real exec")
    plt.plot(sizes, worst1, "teal",label =" best1"  )
    plt.plot(sizes, worst2, "firebrick",label =" best2")
    plt.plot(sizes, worst3, 'blueviolet', label =" best3" )
    plt.plot(sizes, worst4, 'blueviolet' , label =" best4")
    plt.plot(sizes, worst5, 'blueviolet' , label =" best5")

    #plt.xlabel('input size (n)')
    #plt.xticks(sizes)
    plt.legend()
    plt.show()

run(best_case_input)
#run(worst_case_input)
#run(average_case_input)
#print_all()
plot_best()

        





