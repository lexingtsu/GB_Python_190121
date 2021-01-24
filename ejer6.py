#Елена Лазарева
#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
entrar_km = float(input("Введите дневную продолжительность бега:"))
total_km = float(input("Введите необходимую продолжительность бега за период:"))
dia = 1
bruto_km = entrar_km
while bruto_km < total_km:
    print(f"За {dia}-й день спортсмен пробежит {entrar_km:.2f}км, а всего - {bruto_km:.1f}км")
    entrar_km += entrar_km * 0.1
    dia += 1
    bruto_km = bruto_km + entrar_km
print(f"Спортсмен добьется общего результата в беге более {total_km:.0f} км за {dia} дней, т.к. пробежит {bruto_km:.1f}км")