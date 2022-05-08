information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
foods = ["된장찌개", "피자", "제육볶음"] 

print(information.get("취미"))

information["특기"] = "피아노"
information["사는곳"] = "서울" ## 딕셔너리 추가
del information["좋아하는 음식"] ## 딕셔너리 삭제
print(information) 
print(len(information)) ## 딕셔너리의 길이
information.clear() ## 딕셔너리를 다 비움

print(information)

print(foods[-2]) ##foods 리스트의 첫 번째가 출력(단, 0이 시작)
foods.append("김밥")
del foods[1]
print(foods)