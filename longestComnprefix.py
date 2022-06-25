if len == 0 or len == 1:
    print("")
else:
    strs.sort()
    result = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            result += strs[0][i]
        else:
            break
return result
