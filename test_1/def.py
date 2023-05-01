import random

# def my_sum(a, b):
#     result = a + b
#     print("두 정수의 합은:", result)

# def my_sum(a, b):
#     return a + b





# options = ['가위', '바위', '보']
# computer_choice = random.choice(options)
# def match_result():
#     while True:
#         user_input = input("가위, 바위, 보 중에서 골라주세요: ")
#         if user_input in options:
#             break
#         else:
#             print("잘못 입력하셨습니다.")
#     return user_input

# user = match_result()
# print(f'플레이어는 {user}를 선택, 컴퓨터는 {computer_choice}를 선택')

# def match(user, computer_choice):
#     if user == computer_choice:
#         if computer_choice == '가위':
#             print("비겼다.")
#         elif computer_choice == '바위':
#             print("졌다.")
#         else:
#             print("이겼다.")
        
#     elif user == '바위':
#         if computer_choice == '가위':
#             print("이겼다.")
#         elif computer_choice == '바위':
#             print("비겼다.")
#         else:
#             print("졌다.")
#     else:
#         if computer_choice == '가위':
#             print("졌다.")
#         elif computer_choice == '바위':
#             print("이겼다.")
#         else:
#             print("비겼다.")





def solution(n):
    answer = 0
    for i in range(2, n):
        print(i)
        
        if n % i == 1:
            return i
        print(n)
    return answer          
solution(n)
n = 12
def solution(n):
    x = 2
    while n % x != 1:
        print(x) 
        x += 1
        print(x)  
    return x
solution(n)