a = int(input("ввидите ваше число:"))
h = a // 3600
m = (a // 60) % 60
s = a % 60
if h < 10:
    h = "0" + str(h)
else:
    h = str(h)
if m < 10:
    m = "0" + str(m)
else:
    m = str(m)
if s < 10:
    s = "0" + str(s)
else:
    s = str(s)
print(str(h), "ч. " + str(m), "мин. " + str(s), "сек.")
