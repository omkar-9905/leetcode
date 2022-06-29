k = []
a = ""
for i in range(len(s)):
    a+=s[i]
    k.append(len(a))
    for j in range(i+1,len(s)):
        if s[j] not in a:
            a+=s[j]
            k.append(len(a))
        else:
            k.append(len(a))
            break
    a = ""
if s == "":
    return 0
elif s == " ":
    return 1
else:
    return max(k)
