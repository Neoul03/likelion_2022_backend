menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])

menu3 = menu1 | menu2 #합집합
menu3 = menu1 & menu2 #교집합
menu3 = menu1 - menu2 #차집합

print(menu3)