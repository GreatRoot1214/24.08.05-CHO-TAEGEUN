import random, time

_dict = {'1' :'   ','2' :'   ', '3' :'   ', '4' :'   ', '5' :'   ', '6' :'   ', '7' :'   ', '8' :'   ', '9' :'   '}

def makelist(z) :
  _list = []
  for i in z : 
    _list.append(i)
  return _list
  
_list = makelist(_dict.keys())

if _list == [] :
  choice = 0
def printdict(_dict) :
  print(_dict['7'] + '│' + _dict['8'] + '│' + _dict['9'])
  print('───┼───┼───')
  print(_dict['4'] + '│' + _dict['5'] + '│' + _dict['6'])
  print('───┼───┼───')
  print(_dict['1'] + '│' + _dict['2'] + '│' + _dict['3'])

def selectO(a) :
  _dict[a] = " O "

def selectX(a) :
  _dict[a] = " X "

# 게임 시작
print("Tic-Tac-Toe 게임을 시작합니다!")
printdict(_dict)
print("돌을 놓을 위치를 선택해주세요.(1 ~ 9 사이의 숫자로 선택)")

while True :
  user = input()

  
  if int(user) >= 10 :
    print("1부터 9사이의 숫자를 입력해주세요.")
    printdict(_dict)
  elif user not in _list :
    print("이미 돌이 있습니다. 다른 위치를 선택해주세요")
    printdict(_dict)
  else :
    selectO(user)
    _list.remove(user) 
    printdict(_dict)
    if len(_list) == 0 :
      print("게임이 끝났습니다. 엔터를 누르시면 창을 닫습니다.")
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
    selectX(choice)
    _list.remove(choice) 
    printdict(_dict)
  
  if len(_list) == 0 :
    print("게임이 끝났습니다. 엔터를 누르시면 창을 닫습니다.")
    a = input()
    a = ""
    break
    
