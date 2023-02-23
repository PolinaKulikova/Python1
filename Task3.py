number = str(input("Введите шестизначный номер билета: "))
# a = number[0] + number[1] + number[2]
# b = number[3] + number[4] + number[5]
if number[0] + number[1] + number[2] == number[3] + number[4] + number[5]:
    print("Ваш билет счастливый!")
else: 
    print("Сегодня не ваш день") 