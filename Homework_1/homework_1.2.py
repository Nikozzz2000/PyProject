a = int(input("ввидите ваше число:"))
hour = a // 3600
minutes = (a // 60) % 60
seconds = a % 60
print("%02d:%02d:%02d" % (hour, minutes, seconds))
