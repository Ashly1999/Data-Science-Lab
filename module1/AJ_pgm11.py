a = [35,30,25,15,10]
print("Before sorting array  elements are:")
for i in a:
    print(i, end=" ")
    for i in range(0,len(a)):
        for j in range(+1,len(a)):
            if a[j] < a[i]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp
                print("After array sorting elements:")
                for i in a:
                    print(i,end="")

