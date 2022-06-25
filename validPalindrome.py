a = []
for i in s:
    if i.isalpha() == True or i.isnumeric() == True:
        a.append(i.lower())

if a == a[::-1]:
    return True
else:
    return False
