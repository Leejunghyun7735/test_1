# movie_rank = ["닥터스트레인지","스플릿","럭키"]
# print(movie_rank) # 여러 개의 값을 저장하기 위해 리스트 자료형을 사용!

# movie_rank = ["닥터스트레인지","스플릿","럭키"]
# movie_rank.append("베트맨")# append를 사용해서 추가!
# print(movie_rank)

# movie_rank = ["닥터스트레인지","스플릿","럭키"]
# movie_rank.insert(1,"슈퍼맨")# insert를 사용하면 특정위치에 끼어 넣기가 가능
# print(movie_rank)

# movie_rank = ["닥터스트레인지","슈퍼맨","스플릿","럭키","배트맨"]
# del movie_rank[3]# del를 사용해 특정위치의 값을 삭제할 수 있다.
# print(movie_rank)

# movie_rank = ["닥터스트레인지","슈퍼맨","스플릿","럭키","배트맨"]
# del movie_rank[2]# [2,4] 안됨x
# del movie_rank[2]# [2] 하나 더 만들어서 시도. 그런데 이값은 지워지면 순서를 다시 세어줘야한다.
# print(movie_rank)

# #최댓값 최소값
# nums = [1,2,3,4,5,6,7]
# print("max", max(nums))
# print("min", min(nums))

# #더하기
# nums = [1,2,3,4,5]
# print("sum",sum(nums))

# #데이터의 개수 구하기
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# #평균 구하기
# nums = [1, 2, 3, 4, 5]
# average = sum(nums) / len(nums)# 15/5
# print(average)

# #날짜 정보를 제외하고 가격 정보만을 출력하라
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# #날짜 정보를 제외하고 가격 정보만을 출력하라
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# del price[0]
# print(price)

# # 홀수 출력
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# # 
# nums = [1,2,3,4,5,6,7,8,9,10]
# print = (nums[1::2])





# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# del price[0] # 한 개만 삭제 가능 del
# print(price)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])


# interest = ['삼성전자', 'LG전자', 'Naver']
# del interest[1]
# print(interest)


# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(interest[0],interest[1],interest[2],interest[3],interest[4]) 


# 리스트를 벗겨라!
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest)) 


#ex)
# animals = ['사자', '코끼리', '기린', '원숭이', '바나나원숭이']

# print " ".join(animals)
# >> 사자,코끼리,기린,원숭이,바나나원숭이 


#Join 함수는 리스트를 특정 구분자를 포함해 문자열로 변환해 주는 함수입니다. 
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("/".join(interest)) 


# 줄바꿈
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest)) 


# string = "삼성전자/LG전자/Naver"
# print(string.split("/"))
# #######################
# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)


########sort 정렬######## 함수전체가 변형
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)


# # sorted 함수가 변형되지않음 (선호!)
# data = [2, 4, 3, 1, 5, 10, 9]
# at = sorted(data)
# print(at)



#*valid_score, _, _= scores _변수가 저장된다 별 표현식
#좌측
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, b, c= scores
# print(valid_score)

#우측
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score= scores
# print(valid_score)

# 가운데
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,*valid_score,c = scores
# print(valid_score)


#{"a" : 1, "b":2}  key 명칭 value 값이다. key:value

# immutable 변동 o 
# mutable 변동 x (key 에러 )


# a = """dsddsd"""
# print(a)


#######
# a= 2 
# print(id(a))
# a= 3
# print(id(a))

# a= 2 
# print(id(2))
# a= 3
# print(id(3))




# a = [1,2,3,4,5,6]
# del a[1::2]
# print(a)

num = 0

while num <5:
    print(num)
    num = num + 1
    