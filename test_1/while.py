import random



# a == 0


# while a == 0:
#     print()

# pop(제일 마지막의 원소가 나온다.)
#append는 더해주고 pop은 빼준다라고 생각하자.


# my_list = [ {"이름":"권기현", "나이":32}, 
#      {"이름":"홍서연", "나이":20}, 
#      {"이름":"박소진", "나이":20}, 
#      {"이름":"이미진", "나이":19}, 
#      {"이름":"이정현", "나이":18},
#       {"이름":"연제건", "나이":17}, 
#  {"이름":"강유지", "나이":16}, 
#  {"이름":"김태연", "나이":15}, 
#  {"이름":"김주영", "나이":14}]



# while my_list:
#     a = my_list.pop()
#     if a["이름"] == "이정현":
#         print(a["이름"])
#         break
# print(len(my_list))



# answer = 46


# while True:
#     user_input = int(input())
#     if user_input == answer:
#         print("정답입니다")
#     else:
#         print("틀렸습니다")






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





























# while len(my_list) > 5:
#     my_list.pop()    
#     print(my_list)
#     break



# i = 0
# while i > 5:
#     i += 1
#     my_list.pop([i])
#     print(my_list)



# while len(my_list) > 5:
#     my_list.pop()
#     if len(my_list) == 5:
#         print(my_list)
#         break


# my_list.pop()
# print(len(my_list))