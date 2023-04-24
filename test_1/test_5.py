import random



answer = random.randint(10, 100)
while True:
    user_input = int(input())
    if user_input == answer:
        print("정답입니다")
        break
    elif user_input < answer:
        print("up")
    else:
        print("down")
print("게임이 끝났습니다.")

  
 
T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split()) 
    result = a + b
    print(f"Case #{i}: {result}")  







# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.


while True:  
    a, b = map(int, input().split())  
    if a == 0 and b == 0:  
        break
    print(a + b)  