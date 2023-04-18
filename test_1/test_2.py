### 2023-04-18 숙제 ###



#문제 :n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
sum = 0
for i in range(n+1):
    sum += i
print(sum)

# 문제점 : (input("n")) str 값을 넣으면 틀렸다고 나옴

# 시도 : str을 다 빼고 제출하니 정답이였다.

# 알게된 점 : 정답은 맞지만 문제에서 요구하는 바를 정확하게 짚어야하는거 같다.



# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.


T= int(input())

for i in range(T):
    A,B = map(int,input().split())
    print(A+B)
     
# 문제점 :  A,B = map(int,input().split()) 를 반복문에 돌려줄 생각을 전혀 못했음
# 시도 : 
# T= int(input())
# A,B = map(int,input().split())

# for i in range(T):
    
#     print(A+B) 
# 처음에 이런식으로 함. 
# 하지만 결과값이 제대로 나오지않아 반복문에 A,B = map(int,input().split()) 넣어 봤다.


# 해결 : for 문에서 T값이 3이다 라고하면 A,B = map(int,input().split() 3번의 덧셈을 함.
# 알게된점 : for문이 어떻게 돌아가는지 예측이 가능했다.






