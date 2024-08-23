_dict = {'1' :'   ','2' :'   ', '3' :'   ', '4' :'   ', '5' :'   ', '6' :'   ', '7' :'   ', '8' :'   ', '9' :'   '}

def makelist(z) :
  _list = []
  for i in z : 
    _list.append(i)
  return _list
  
_list = makelist(_dict.keys())

print(_list[1])