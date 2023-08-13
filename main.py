# статический метод посмотреть теорию
# raise для описания своих ошибок
# while True:
#     try:
#         login = input('Введите логин: ')
#         if len(login) <= 3:
#             raise Exception('Введен короткий логин повторите ввод')
#         if len(login) >= 30:
#             raise Exception('Введен длинный логин повторите ввод')
#
#         break
#     except Exception as error:
#         print(f'Ошибка {error}')
# try:
#     password = input('Введите пароль: ')
#     if len(password) >= 8:
#         raise Exception('Введен не верный пароль повторите ввод')
# except Exception as error:
#     print(error)
# print(f'Вы ввели логин такой: {login} и пароль: {password}')

import os

cars = []
with open('text.txt', 'r') as textFile:
    someCars = textFile.readlines()
    cars = [car.rstrip('\n') for car in someCars]

while True:
    print('0 - Выход')
    print('1 - Количество автомобилей на стоянке')
    print('2 - Добавить автомобиль на стоянку')
    print('3 - Убрать автомобиль со стоянки')

    option = input('Выберите действие из списка: ')

    if option == '0':
        with open('text.txt', 'w') as textFile:
            textFile.writelines([car + '\n' for car in cars])
        break
    elif option == '1':
        print('Количество автомобилей на стоянке')
        for car in cars:
            print(' - ' + car)

    elif option == '2':
        car = input('Введите автомобиль для добавления на стоянку: ')
        cars.append(car)
        print('Автомобиль добавлен на стоянку ' + car)

    elif option == '3':
        print(cars)
        # car = input('Выберите автомобиль для выезда со стоянки: ')
        car1 = int(input('Выберите автомобиль для выезда со стоянки по индексу: '))
        cars.pop(car1)
        print(f'Автомобиль {cars} уехал со стоянки ')


    os.system('Ожидание')
    os.system('cls')

print('Пока')
