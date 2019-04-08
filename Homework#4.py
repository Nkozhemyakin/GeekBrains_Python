import random
import re

# HM#4.1.1
print ('HM#4.1.1')


my_list = [random.randint(-10, 10) for _ in range(4)]
new_list = [i ** 2 for i in my_list]
print(my_list)
print (new_list)

# HM#4.1.2
print ('HM#4.1.2')

fruits_1 = ['��������','������','�����','��������']
fruits_2 = ['��������', '��������', '��������', '�����']

new_list = [i for i in fruits_2 if i in fruits_1]
print(new_list)

# HM#4.1.3
print ('HM#4.1.3')

my_list = [random.randint(-100, 100) for _ in range(10)]
print(my_list)
new_list = [i for i in my_list if i % 3 == 0 and i >= 0 and i % 4 != 0]
print(new_list)

# HM#4.2.1
print ('HM#4.2.1')

name = input('Enter your name: ')
last_name = input('Enter your last name: ')
email = input('Enter your email: ')

name_error = re.search('^[A-Z�-ߨ0-9]{1}', name) is not None
last_name_error = re.search('^[A-Z�-ߨ]{1}', last_name) is not None
email_error = re.match(r'[a-z0-9]+@[a-z]+\.[ru,com,org]{2,3}', email) is not None

print('All of the information is correct!' if name_error and last_name_error and email_error else '������ ������� �������!')
print('Wrong name' if name_error == False else '')
print('Wrong email' if last_name_error == False else '')
print('Wrong email' if email_error == False else '')


# HM#4.2.2
print ('HM#4.2.2')

some_str = '''
����� � ������; ���� ��������!
��� �� ��������, ���� ���������� �
����, ���������, ��������:
������ �������� ����� �����
��������� �������� ������,
������� ������ �����!
�����, �� �������, ����� �������,
�� ������ ���� ���� ��������;
����, ��� ������� �����,
������ ���� ������� �������,
� �� ��������� ������ �
� �����... ������� � ����:
��� �������� ��������
������������� �������,
������ �� ������, ���� �����;
���������� ��� ���� �������,
� ��� ������ ���� ��������,
� ����� ���� ����� �������.
��� ������� �������� �������
�������. ������� �������
������ ����������� ����.
������� ������ � �������.
�� ������: �� ������ �� � �����
������� ����� �������?
������� �� ��������� �����,
���� �����, ���������� ����
������������� ����
� �������� ���� ������,
����, ������� ����� ������,
� �����, ����� ��� ����.'''

str = re.search(r'\.{2,}', some_str) is not None
print('The text contains more than one dot in a row.' if str else 'The text does not contain more than one dot in a row.')
