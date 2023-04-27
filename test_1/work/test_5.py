import random
# 업다운 
count = int(input("반복할 횟수:"))
i = 1
answer = random.randint(10, 100)
while True:
    user_input = int(input())
    if i == count:
        
        break
    elif user_input == answer:
        print("정답입니다")
        break
    
    elif user_input < answer:
        print("up")
    else:
        print("down")
print("게임이 끝났습니다.")

  

  
#  # 11021번
# T = int(input())


# for i in range(1, T+1):
#     a, b = map(int, input().split()) 
#     result = a + b
#     print(f"Case #{i}: {result}")  




# # # 10952번
# while True:  
#     a, b = map(int, input().split())  
#     if a == 0 and b == 0:  
#         break
#     print(a + b)  







