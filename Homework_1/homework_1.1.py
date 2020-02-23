import datetime
t = datetime.datetime.today().strftime("%Y")
today = int(t)
my_age = (today - 1983)
print("Привет! Давай знакомится, меня завут Нико")
name = input("А тебя?-")
print("Привет", name)
d = input("а кокого числа у тебя день рождения?-")
m = input("а в каком месяце?-")
print(m, "-это круто")
y = input("а в каком году ты родился?-")
year = int(y)
age = (today - year)
s = (my_age - age)
n = (age - my_age)
if age < my_age:
    print("ух ты, это тебе", age, "и ты на", s, "младше меня")
elif age > my_age:
    print("ух ты, это тебе", age, "и ты на", n, "старше меня")
else:
    print("ух ты, так тебе тоже", age, "и мы ровесники")
print("Ну ладно, мне пора, а", d, m, "принесу тебе торт с", age, "свечами :)")
