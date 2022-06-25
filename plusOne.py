def stringToList(ans):
  return [char for char in ans]

s = int(''.join(str(x) for x in digits))
ans = str(s+1)

fnl_ans = stringToList(ans)
return fnl_ans
