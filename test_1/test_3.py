#문제:시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.


score = int(input())

if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")

# 문제점 : for문을 사용해서 해야하나? 라는 생각으로 시행착오를 겪음
# 해결 : if문으로 간단하게 끝 낼 수 있다는 생각으로 input을 사용해서 해결!