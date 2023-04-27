
# 숙제1
# 가위 바위 보 게임
#import random

# options = ['가위', '바위', '보']
# computer_choice = random.choice(options)

# ~~~~~~유저의 입력을 받는다~~~~

# print("당신은 ", user_input, "를 냈습니다.")
# print("컴퓨터는 ", computer_choice, "를 냈습니다.")
# import random

import random

options = ['가위', '바위', '보']
computer_choice = random.choice(options)

while True:
    user_input = input('가위, 바위, 보 중에서 골라주세요: ')
    if user_input not in options:
        print('다시 입력하세요.')
        continue

    if user_input == computer_choice:
        print('비겼습니다.')
    elif user_input == '가위':
        if computer_choice == '바위':
            print('졌습니다.')
            break
        else:
            print('이겼습니다!')
            break
    elif user_input == '바위':
        if computer_choice == '보':
            print('졌습니다.')
            break
        else:
            print('이겼습니다!')
            break
    elif user_input == '보':
        if computer_choice == '가위':
            print('졌습니다.')
            break
        else:
            print('이겼습니다!')
            break

print(f'당신은 {user_input}를 냈습니다.')
print(f'컴퓨터는 {computer_choice}를 냈습니다.')


#숙제2
#문제
#준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.
#영수증에 적힌,
#구매한 각 물건의 가격과 개수
#구매한 물건들의 총 금액
#을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.


x = int(input()) 
n = int(input()) 
total = 0

for i in range(0,n):
    a,b= map(int,input().split())
    total += a*b

if total == x:
    print("YES")
else:
    print("NO")


