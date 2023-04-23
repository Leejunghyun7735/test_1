###########

class Human():
         #생성자
    def __init__(self,이름,나이,성별):
        self.이름 = 이름
        self.나이 = 나이
        self.성별 = 성별

    def who(self):
        print(f"이름:{self.이름},나이:{self.나이},성별:{self.성별}")

이름 = Human("이땡땡") 
나이 = Human("이땡땡")
나이 = Human("이땡땡")   



    # def setinfo(self,이름,나이,성별):
    #     self.이름 = 이름
    #     self.나이 = 나이
    #     self.성별 = 성별
    # print(setinfo)

    # def __del__(self):
    #     print('나의 죽음을 알릴 생각을 마라')




# areum = Human("불명","미상","모름")
# areum.who()

# areum.setinfo("정삼삼",270,"울트라")
# areum.who()
# 소멸자!
# areum = Human("정삼삼",270,"울트라")
# del areum



# class OMG:
#     def print(): #여기 무언가를 추가
#         print("oh")

 
# mys = OMG()
# print(mys)

# class stock:
#     def __init__(self,이름,숫자,PER,PBR,배당수익률):
#         self.이름 = 이름
#         self.숫자 = 숫자
#         self.PER = PER
#         self.PBR = PBR
#         self.배당수익률 = float(배당수익률)
        
        
    
#     def set_name(self,이름):
#         self.이름= 이름
    
#     def set_name(self,숫자):
#         self.이름= 숫자
    
    
#     def set_code(self):
#         return self.숫자
    
#     def set_name(self):
#         return self.이름

# 배당수익률=stock("삼성전자", "005930", "sdagas", "Adg", 1.1)



