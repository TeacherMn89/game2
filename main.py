print('Як називається найвища гора світу?')
print('1 - Ельбрус, 2 - Мауна-Лоа, 3 - Еверест, 4 - Деналі')


while True:    
    answer = input()
    try:
        answer = int(answer)
        break
    except:
        print('Помилка! Введіть номер правильної відповіді')
if answer == 3:
    print('Абсолютно вірно!')
else:
    print('Ні. Еверест, 8848 метрів')
