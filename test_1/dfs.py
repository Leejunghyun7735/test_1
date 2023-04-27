arr1=[[1,2],[2,3],[1,1]]
arr2 = [[3,4],[5,6],[1,1]]
#result1=[[4,6],[7,9]]

a1=arr1[0][0]+arr2[0][0]# 4
a2=arr1[0][1]+arr2[0][1]#6
a3=arr1[1][0]+arr2[1][0]#7
a4=arr1[1][1]+arr2[1][1]#9
a5=arr1[2][0]+arr2[2][0]
a6= arr1[2][1]+arr2[2][1]
result1= [[a1,a2],[a3,a4],[a5,a6]]


print(result1)

# print(arr1[0][1]) # [][] 이중?

# for i in range(len(arr1)):
#     a = []
#     print()
# test = arr1[0]+arr2[0]
# print(test)