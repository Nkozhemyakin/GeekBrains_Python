from math import sqrt
from random import randint

print ("HM#2 1.1")
fruits = ["������", "�����", "����", "�����"]
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
    '01': '������', '02': '������', '03': '������', '04': '���������', '05': '�����',
    '06': '������', '07': '�������', '08': '�������', '09': '�������', '10': '�������',
    '11': '������������', '12': '�����������', '13': '�����������', '14': '�������������',
    '15': '�����������', '16': '������������', '17': '�����������', '18': '�������������',
    '19': '�������������', '20': '���������', '21': '�������� ������', '22': '�������� ������',
    '23': '�������� ������', '24': '�������� ���������', '25': '�������� �����', '26': '�������� ������',
    '27': '�������� �������', '28': '�������� �������', '29': '�������� �������', '30': '���������',
    '31': '�������� ������'
}

month = {
    '01': '������', '02': '�������', '03': '�����', '04': '������', '05': '���', '06': '����',
    '07': '����', '08': '�������', '09': '��������', '10': '�������', '11': '������', '12': '�������'
}

data = input ("Enter your date in format dd.mm.yyyy: ")
parts = data.split('.')
print('{} {} {}'.format(day[parts[0]], month[parts[1]], parts[2] + " ����"))

print('HM#2. 2.3')

n = randint(10, 15)
random_list = [randint(-100, 100) for i in range(n)]
print(random_list)