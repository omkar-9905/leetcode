new = "".join(s.rstrip())
ptr = 0
if " " not in new:
    return len(new)
else:
    for i in range(len(new)-1,-1,-1) :
        if s[i] == " ":
            return ptr
        else:
            ptr+=1
