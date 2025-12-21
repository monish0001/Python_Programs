class sumOfArray:
    def sum(selft,arr):
        total=0
        for i in arr:
            total+=i
        return total
    
    

if __name__=="__main__":
    n=int(input("size of array: "))
    arr=[]
    for i in range(n):
        x=int(input(f"element {i+1}: "))
        arr.append(x)   
    ob=sumOfArray()
    print(ob.sum(arr))