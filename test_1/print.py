from datetime import datetime

# # data= datetime(2023,2,2)
# # today= data.strftime(" %Y년 %m월 %d일")

#  my_name = input()
#  print(f"{my_name}님 안녕하세요! 오늘은{today}입니다")


my_list = [ {"이름":"권기현", "나이":32},  
           {"이름":"홍서연", "나이":20},  
           {"이름":"박소진", "나이":20}, 
           {"이름":"이미진", "나이":19},  
           {"이름":"이정현", "나이":18},
             {"이름":"연제건", "나이":17}, 
    {"이름":"강유지", "나이":16}, 
    {"이름":"김태연", "나이":15}, 
    {"이름":"김주영", "나이":14}]


# ~~님 ~~님 ~~님 안녕하세요
# for person in my_list:
#     if 20 <= person["나이"]:
#         print(f"{person['이름']}님", end=' ')

# print("안녕하세요")

#     if person["이름"] == "이정현" or person["이름"] == "권기현":
#         person["나이"] -= 1
#     else:
#         person["나이"] += 100
    
#  print(f"person{'이름'}님 반갑습니다!")




a = list(map(int,input().split()))

for i in a:
    print(a,end='')


    