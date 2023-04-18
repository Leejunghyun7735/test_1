movie_rank = ["닥터스트레인지","스플릿","럭키"]
print(movie_rank) # 여러 개의 값을 저장하기 위해 리스트 자료형을 사용!

movie_rank = ["닥터스트레인지","스플릿","럭키"]
movie_rank.append("베트맨")# append를 사용해서 추가!
print(movie_rank)

movie_rank = ["닥터스트레인지","스플릿","럭키"]
movie_rank.insert(1,"슈퍼맨")# insert를 사용하면 특정위치에 끼어 넣기가 가능
print(movie_rank)

movie_rank = ["닥터스트레인지","슈퍼맨","스플릿","럭키","배트맨"]
del movie_rank[3]# del를 사용해 특정위치의 값을 삭제할 수 있다.
print(movie_rank)

movie_rank = ["닥터스트레인지","슈퍼맨","스플릿","럭키","배트맨"]
del movie_rank[2]# [2,4] 안됨x
del movie_rank[2]# [2] 하나 더 만들어서 시도. 그런데 이값은 지워지면 순서를 다시 세어줘야한다.
print(movie_rank)

#최댓값 최소값
nums = [1,2,3,4,5,6,7]
print("max", max(nums))
print("min", min(nums))

#더하기
nums = [1,2,3,4,5]
print("sum",sum(nums))

#데이터의 개수 구하기
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#평균 구하기
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)# 15/5
print(average)

#날짜 정보를 제외하고 가격 정보만을 출력하라
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#날짜 정보를 제외하고 가격 정보만을 출력하라
price = ['20180728', 100, 130, 140, 150, 160, 170]
del price[0]
print(price)

# 홀수 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 
nums = [1,2,3,4,5,6,7,8,9,10]
print = (nums[1::2])







#x = y 양수 제1사분면
#x(음수) = y(양수) 제2
#x = y 음수 제3사분면
#x(양수)) = y(음수) 제2

