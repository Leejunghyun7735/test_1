# a, b= input().split()
# a = int(a[::-1])
# b = int(b[::-1])


# print( max(a,b))

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
def solution(sizes):
    a = 0   
    w = 0 # 초기값! 비교하기 위함이다 0, max 60
    h = 0
    for i in sizes:
        w = max(w,max(i)) 
        print(w) 
        h = max(h,min(i))       
    a = w * h
    return a
solution(sizes)


#h = max(h,min(i))  
60 , 50
70 , 30
60 , 30
80 , 40

14 , 4
19 , 6
16 , 6
18 , 7
11 , 7


10 , 7
12 , 3
15 , 8
14 , 7
15 , 5




arr = [1,1,1,2,3,3,3,5,4,4,5,6]

def solution(arr):
    answer = [arr[0]]
    print(answer)
    for a in arr:         
        if not a == answer[-1]: #!= not 은 같다. += -=
            answer.append(a)
            print(answer)
    return answer
solution(arr)
        




def solution(id_pw, db):
    for i in db:
        if id_pw == i:
            return 'login'
            
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] != i[1]: 
            return 'wrong pw'
        else:
            return 'fail'
            
    




# 로그인 
def solution(id_pw, db):
    for i in db:
        if id_pw == i:
            return 'login'
            
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] != i[1]: 
            return 'wrong pw'
    
    return 'fail'
     
#for 이중구문으로 사용




     


#  순서대로 중복된 값을 제거하고 뒤에있는 중복된 값도 출력해라
# # set



    
# arr = [1, 1, 3, 3, 0, 1, 1]
# result = list(set(arr))

# def solution(arr):
#     answer = [arr[0]]1   
#     for a in arr:
#         if not a == answer[-1]: 1
                
#             answer.append(a)
#             print(answer)

#     return answer
# arr = [1,1,2,3,3,5,3,3,4,10,10]


T = int(input())

for i in range(T):
    a = input()
print(a[0]+a[-1])

#
