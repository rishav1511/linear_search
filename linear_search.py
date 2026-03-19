import timeit
import matplotlib.pyplot as plt
def Input(Array,n):
    for i in range(n):
        ele=int(input("Enter the no of element: "))
        Array.append(ele)
def linear_search(Array,key):
    for x in Array:
        if x==key:
            return True
    return False
N=[]
CPU=[]
trail=int(input("Enter the number of trail: "))
for t in range(trail):
    Array=[]
    print("---Trail number---",t+1)
    n=int(input("Enter number of elements: "))
    Input(Array,n)
    print("Array= ",Array)
    key=int(input("Enter the element you want to search: "))
    start=timeit.default_timer()
    s=linear_search(Array,key)
    end=timeit.default_timer()
    print("Element found: ",s)
    tim=end-start
    N.append(n)
    CPU.append(round(tim*1000000,2))
print("\nN CPU")
for t in range(trail):
    print(N[t], CPU[t])
plt.plot(N,CPU)
plt.scatter(N,CPU,marker="*")
plt.xlabel("Array size N")
plt.ylabel("CPU processing time in Microseconds")
plt.title("Time complexity of linear search")
plt.show()

