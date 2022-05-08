import random

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

print(lunch)

while True: 
    flag1 = input ("추가를 계속하시겠습니까?(Y/N) : ")
    if flag1 == "N" or flag1 == "n":
        break
    
    item = input ("음식을 추가 해주세요 : ")
    lunch.append(item)
    print(lunch)
    
    
    
while True:
    flag2 = input ("삭제를 계속하시겠습니까?(Y/N) : ")
    if flag2 == "N" or flag2 == "n":
        break
    
    delete = input ("음식을 삭제 해주세요 : ")
    lunch = set(lunch) - set([delete])
    print (lunch)
    
menu = random.choice(lunch)

print("오늘 메뉴는 "+ menu +"입니다.")