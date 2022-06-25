def stringToList(ans):
 return [char for char in reversed(ans)]
binary_a = stringToList(a)
binary_b = stringToList(b)
def toNum(num):
    sum_a = []
    for i,j in enumerate(num):
        if j == "1":
            sum_a.append(2**i)
    return sum(sum_a)
num_a = toNum(binary_a)
num_b = toNum(binary_b)
final_num_sum = num_a + num_b
def decimalToBinary(n):
    return "{0:b}".format(int(n))
s = decimalToBinary(final_num_sum)
return s
