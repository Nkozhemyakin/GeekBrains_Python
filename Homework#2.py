from math import sqrt
from random import randint

print ("HM#2 1.1")
fruits = ["яблоко", "банан", "киви", "арбуз"]
for i, item in enumerate(fruits):
    print(i +1, item)

print ("HM#2 1.2")
b = {'a', 'b', 'c', 'c', 'a', 'e'}
d = {'a', 'b', 'c', 'd'}
c = b - d
print(list(c))

print ("HM#2 1.3")
first_list = [2, 7, 5, 6, 9, 15]
print (first_list)
new_list = []
last_name = len(first_list)
for i in range(last_name):
    if first_list[i] % 2 == 0:
        new_list.append(first_list[i] / 4)
    else:
        new_list.append(first_list[i] * 2)
        print("New list is:", new_list)


print ("HM#2 2.1")
hm221b = [4, 2, 9, 3, 25, 36]
hm221n = []
print ("Old list: ", hm221b)
for each in hm221b:
    if each > 0 and (sqrt(each) - int(sqrt(each)) == 0):
        hm221n.append(int(sqrt(each)))
print ("New list: ", hm221n)

print('HM#2. 2.2')

day = {
    '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
    '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
    '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
    '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
    '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
    '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
    '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое',
    '31': 'тридцать первое'
}

month = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
    '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
}

data = input ("Enter your date in format dd.mm.yyyy: ")
parts = data.split('.')
print('{} {} {}'.format(day[parts[0]], month[parts[1]], parts[2] + " года"))

print('HM#2. 2.3')

n = randint(10, 15)
random_list = [randint(-100, 100) for i in range(n)]
print(random_list)