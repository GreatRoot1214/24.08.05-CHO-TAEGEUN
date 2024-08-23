# 틱택토 만들기

#   │  │
# ──┼──┼──
#   │  │
# ──┼──┼──
#   │  │

# 사전 설정
import random, time
_dict = {'1':'   ','2':'   ','3':'   ','4':'   ','5':'   ','6':'   ','7':'   ','8':'   ','9':'   '}
_list2 = _dict.keys()
_list = []

user = input()
for i in _list2 :
  _list.append(i)

if _list == [] :
  choice = 0
def printdict(_dict) :
  print(_dict['7'] + '│' + _dict['8'] + '│' + _dict['9'])
  print('───┼───┼───')
  print(_dict['4'] + '│' + _dict['5'] + '│' + _dict['6'])
  print('───┼───┼───')
  print(_dict['1'] + '│' + _dict['2'] + '│' + _dict['3'])

def select(a) :
  _dict[a] == " X "
  _list.remove[a]
    
# 게임 시작
print("Tic-Tac-Toe 게임을 시작합니다!")
printdict(_dict)
print("돌을 놓을 위치를 선택해주세요.(1 ~ 9 사이의 숫자로 선택)")

while True :
  user = int(input()) 

  if user >= 10 :
    print("1부터 9사이의 숫자를 입력해주세요.")
    printdict(_dict)
  elif user not in _list :
    print("이미 돌이 있습니다. 다른 위치를 선택해주세요")
    printdict(_dict)

  else :
    if user in _list :
      select(user)
      
    elif len(_list) == 0 :
      break
    printdict(_dict)
    if len(_list) == 0 :
        print("게임이 끝났습니다. 엔터를 누르시면 창을 닫습니다.")
        a = input()
        a = ""
        break
    elif _dict('1','2','3') == ' O ' :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif _dict('4','5','6') == ' O ' :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif _dict('7','8','9') == ' O ' :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line1[0] == "ㅇ" and line3[0] == "ㅇ" and line5[0] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[2] == "ㅇ" and line3[2] == "ㅇ" and line5[2] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅇ" and line3[4] == "ㅇ" and line5[4] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[0] == "ㅇ" and line3[2] == "ㅇ" and line5[4] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅇ" and line3[2] == "ㅇ" and line5[0] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.") 
      a = input()
      a = "" 
      break
    elif line1.count("ㅁ") == 3 :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line3.count("ㅁ") == 3 :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line5.count("ㅁ") == 3 :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line1[0] == "ㅁ" and line3[0] == "ㅁ" and line5[0] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[2] == "ㅁ" and line3[2] == "ㅁ" and line5[2] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅁ" and line3[4] == "ㅁ" and line5[4] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[0] == "ㅁ" and line3[2] == "ㅁ" and line5[4] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅁ" and line3[2] == "ㅁ" and line5[0] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.") 
      a = input()
      a = "" 
      break
    
    choice = random.choice(_list)
    
    time.sleep(0.5)
    print("")
    print("다음은 제 차례입니다.")
    print("")
    time.sleep(0.5)
    

    if choice in _list :
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
    if len(_list) == 0 :
        print("게임이 끝났습니다. 엔터를 누르시면 창을 닫습니다.")
        a = input()
        a = ""
        break
    elif line1.count("ㅇ") == 3 :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line3.count("ㅇ") == 3 :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line4.count("ㅇ") == 3 :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[0] == "ㅇ" and line3[0] == "ㅇ" and line5[0] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[2] == "ㅇ" and line3[2] == "ㅇ" and line5[2] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅇ" and line3[4] == "ㅇ" and line5[4] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[0] == "ㅇ" and line3[2] == "ㅇ" and line5[4] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅇ" and line3[2] == "ㅇ" and line5[0] == "ㅇ" :
      print("당신의 승리입니다. 축하드립니다. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1.count("ㅁ") == 3 :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line3.count("ㅁ") == 3 :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line5.count("ㅁ") == 3 :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")
      a = input()
      a = ""
      break
    elif line1[0] == "ㅁ" and line3[0] == "ㅁ" and line5[0] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[2] == "ㅁ" and line3[2] == "ㅁ" and line5[2] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅁ" and line3[4] == "ㅁ" and line5[4] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[0] == "ㅁ" and line3[2] == "ㅁ" and line5[4] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.")  
      a = input()
      a = ""
      break
    elif line1[4] == "ㅁ" and line3[2] == "ㅁ" and line5[0] == "ㅁ" :
      print("당신의 패배입니다. 멍청하시네요. 엔터를 누르면 창을 종료합니다.") 
      a = input()
      a = "" 
      break