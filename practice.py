#Quiz 1
# station = "인천공항"
# print(station,"행 열차가 들어오고 있습니다.")


# print(random()) #0.0~1.0미만의 임의의 값 생성
#randrange , randint

# #Quiz 2
# from random import *
# day = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월",day,"일로 선정되었습니다.")

# sentence = '나는 소년입니다'
# print(sentence)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# 슬라이싱 : 필요한 정보만 가져오는 것
# jumin = "991001-1234567"
# print("연 : " + jumin[-7:]) 맨 뒤에서부터 7번재부터 끝까지

# python = "Python is Amazing"
# print(python.lower()) 다 소문자로
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java")) 글자 바꾸기

# index = python.index("n")
# print(index)
# print(python.find("Java"))
# print(python.index("Java"))
# print("bihihihi")
# print(python.count("n"))

#문자열 포맷
#방법 1
# print("나는 %d살입니다." % 20)
# print("Apple 은 %c로 시작해요." % "A")

# 방법 2
# print("나는 {}살입니다.".format(20))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
# print("저는 \"나도코딩\"입니다.") 탈출문자..
# /r : 커서를 맨앞으로 이동
# /b : 백스페이스(한글자삭제)
# /t : 탭

#Quiz3
# url = "http://google.com"
# my_str = url.replace("http://", "") #규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")] 
# # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(password)

#set
#자료구조의 변경

# absent = [2,5]
# for student in range(1,11):
#     if student in absent:
#         continue #계속해서 다음 반복문 진행
#     print("{0}, 책을 읽어봐".format(student))

# 한줄포문
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# Quis 
# from random import *
# cnt = 0 #총 탑승 승객

# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))   

# print("총 탑승 승객 수 : {0}분".format(cnt))

# def open_account():
#     print("계좌 생성 완료!")

# open_account()

# def std_weight(height, gender):
#     if gender == "M":
#         std_w = height * height * 22
#     else:
#         std_w = height * height * 21

#     return std_w
# height = 175
# std_w = round(std_weight(height / 100, "M"),2)
# print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, std_w))

# print("Python", "Java", sep="   ")yhj

# answer = input("입력하세요 :")
# print("입력값은",answer)

# 다양한 출력포맷

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0점",file=score_file)
# print("영어 : 30점",file=score_file)
# score_file.close()
