#Елена Лазарева
# Поработайте с переменными, создайте несколько, выведите на экран
x = 12
y = 3.1471
z = "Чего тебе надобно, старче?"
v = x + y > 16
w = None
print("переменная х = ", x, type(x))
print("переменная y = ", y, type(y))
print("а вот переменная z = ", z, type(z))
print("переменная v = ", v, type(v))
print("переменная w = ", w, type(w))

# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
name = input("Введите имя: ")
s_name = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
a = int(input("Введите число:"))
print(f"{name} {s_name}, ваш возраст = {age}")
print("Квадрат Вашего числа равен:", a ** 2)
print("А если Ваш возраст сложить с введенным числом, то получится:", a + age)
print("Желаю счастья!")
