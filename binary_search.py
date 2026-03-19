import timeit
import matplotlib.pyplot as plt
def Input(Array,n):
    for i in range(n):
        ele=int(input("Enter the no of element: "))
        Array.append(ele)
def binary_search(Array,key):
    while len(Array)>0:
        mid=len(Array)//2
        if Array[mid]==key:
            return True
        elif Array[mid]<key:
            Array=Array[mid+1:]
        else:
            Array=Array[:mid]
    return False
N=[]
CPU=[]
trail=int(input("Enter the number of trails: "))
for t in range(trail):
    Array=[]
    print("---Trail number---",t+1)
    n=int(input("Enter the number of element: "))
    Input(Array,n)
    Array.sort()
    print("Sorted Array: ",Array)
    key=int(input("Enter the element which you want to search: "))
    start=timeit.default_timer()
    s=binary_search(Array,key)
    end=timeit.default_timer()
    print("Element found: ",s)
    tim=end-start
    N.append(n)
    CPU.append(round(tim*1000000,2))
print("\nN CPU")
for t in range(trail):
    print(N[t],CPU[t])
plt.plot(N,CPU)
plt.scatter(N,CPU,color='red',marker='*')
plt.xlabel("Array size N")
plt.ylabel("CPU processing time in Microseconds")
plt.title("Time complexity of Binary search")
plt.show()