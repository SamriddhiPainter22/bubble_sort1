def bubble_sort(list1):
    for i in range(0,len(list1)-1):
      for j in range(len(list1)-1):
          if (list1[j]>list1[j+1]):
              temp=list1[j]
              list1[j]=list1[j+1]
              list1[j+1]=temp
    return list

list=[6,0,7,4,1,45,23,12,90]

print("The unsorted list of array is: ",list
)
print("The sorted list of array is: ",bubble_sort(list))
