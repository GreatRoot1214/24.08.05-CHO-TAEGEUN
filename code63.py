import random, time
line1 = ["  ","│", "  ", "│", "  "]
line2 = ["──", "┼", "──", "┼", "──"]
line3 = ["  ","│", "  ", "│", "  "]
line4 = ["──", "┼", "──", "┼", "──"]
line5 = ["  ","│", "  ", "│", "  "]
line = [line5, line4, line3, line2, line1]
_list = [1,2,3,4,5,6,7,8,9]


print("Tic-Tac-Toe 게임을 시작합니다!")

for i in line :
  print(*i)

print("돌을 놓을 위치를 선택해주세요.(1 ~ 9 사이의 숫자로 선택)")

while True :
  user = int(input())  
  if user >= 10 :
    print("1부터 9사이의 숫자를 입력해주세요.")
    for i in line :
      print(*i)
  elif user not in _list :
    print("이미 돌이 있습니다. 다른 위치를 선택해주세요")
    for i in line :
      print(*i)
  elif user in _list :
    _list.remove(user) 
    if user == 1 :
      line1[0] = "ㅇ"
    elif user == 2 :
      line1[2] = "ㅇ"
    elif user == 3 :
      line1[4] = "ㅇ"
    elif user == 4 :
      line3[0] = "ㅇ"
    elif user == 5 :
       line3[2] = "ㅇ"
    elif user == 6 :
      line3[4] = "ㅇ"
    elif user == 7 :
      line5[0] = "ㅇ"    
    elif user == 8 :
      line5[2] = "ㅇ"
    elif user == 9 :
      line5[4] = "ㅇ" 
    for i in line :
      print(*i)

  choice = random.choice(_list)
  if choice in _list :
    # time.sleep(0.5)
    print("")
    print("다음은 제 차례입니다.")
    print("")
    # time.sleep(0.5)
    _list.remove(choice)
    if int(choice) == 1 :
      line1[0] = "ㅁ"
    elif int(choice) == 2 :
      line1[2] = "ㅁ"
    elif int(choice) == 3 :
      line1[4] = "ㅁ"
    elif int(choice) == 4 :
      line3[0] = "ㅁ"
    elif int(choice) == 5 :
      line3[2] = "ㅁ"
    elif int(choice) == 6 :
      line3[4] = "ㅁ"
    elif int(choice) == 7 :
      line5[0] = "ㅁ"
    elif int(choice) == 8 :
      line5[2] = "ㅁ"
    elif int(choice) == 9 :
      line5[4] = "ㅁ" 
    for i in line :
      print(*i)
    
