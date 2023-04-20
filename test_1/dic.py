# my_list = ["a","b","c"]
# del my_list[0]
# print(my_list)

# my_list = ["a","b","c"]
# print(my_list[::-1])


# my_list = ["a","b","c","d","e","f"]
# print(my_list[0:5])

# my_list = ["a","b","c","d","e","f"]
# print(my_list[2:])

# my_list = ["a","b","c","d","e","f"]
# print(my_list[3:0:-1])

# my_list = ["a","b","c","d","e","f"]
# print(my_list[::2])

# for i in my_list: # :리스트로 출력됨
#     print(i)

# for i in range(100,0,-1):     # :리스트로 출력됨
#     print(i)

# for i in range(10,0,-3):
#     print(i)



# my_list = ["a","b","c","d","e","f"]
# print(my_list[0,5])

# my_list = ["a","b","c","d","e","f"]
# for i in range(2,0):
#     print(my_list[i])  

# my_list = ["a","b","c","d","e","f"]
# for i in range(3,0,-1):
#     print(my_list[i])

# my_list = ["a","b","c","d","e","f"]
# for i in range(0,0,2):
#     print(my_list[i])




# # end
 
# my_list = ['a', 'b', 'c', 'd', 'e', 'f']

# for i in range(5):
#     print(my_list[i], end=', ')

# print()

# for i in range(2, 6):
#     print(my_list[i], end=', ')

# print()

# for i in [3, 2, 1]:
#     print(my_list[i], end=', ')

# print()

# for i in [0, 2, 4]:
#     print(my_list[i], end=', ')


# 아이스크림 = 1500 
    

# def 별찍기():
#     print("*" * 10)
#     print(" ")
#     print("*" * 10)
#     별찍기() # 

# def 별찍기():
#     print("*" * 10)
#     print(" ")
#     print("*" * 10)
# 별찍기()





#정예반 dict
#추가 부분
# my_dict = {"name":"jung","age":27}
# my_dict["hobby"]= "멜론"
# print(my_dict)
# print(type(my_dict))

# #수정 부분
# my_dict["age"] = 26
# print(my_dict)

# my_dict["name"] = my_dict["name"] -1 
# print(my_dict)


# my_list = [{"이름":"이정현","나이":"24"},{"이름":"이삼삼","나이":"23"},{"이름":"이땡땡","나이":"29"},{"이름":"이일일","나이":"31"},
#            {"이름":"이오오","나이":"27"}]
# names = []
# total_age = 0

# for i in my_list:
#     print(i["이름"])
#     names.append(i["이름"])
#     total_age = total_age + i["나이"]
# print(total_age)

my_list = [ {"이름":"권기현", "나이":32},  
           {"이름":"홍서연", "나이":20},  
           {"이름":"박소진", "나이":20}, 
           {"이름":"이미진", "나이":19},  
           {"이름":"이정현", "나이":18},
             {"이름":"연제건", "나이":17}, 
    {"이름":"강유지", "나이":16}, 
    {"이름":"김태연", "나이":15}, 
    {"이름":"김주영", "나이":14}]

for person in my_list:
    if person["이름"] != "이정현" and person["이름"] != "권기현":
        person["나이"] += 1
        print(my_list)



    


