# selection sort

def selection_sort():
    n = int(input("Enter the total no in an array : "))
    arr = []
    for i in range(n):
        val = input(f"Enter val {i} : ")
        arr.append(val)
    
    for i in range(n):
        mini = i
        for j in range(i+1,n):
            if(arr[mini]>arr[j]):
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
    print("selection sort",arr)

selection_sort()