
# HM#3.1.1
def user_info (name, age, city):
    result = '{}, {} год(а), проживанет в городе {}'.format(name, age, city)
    return result

name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter the city of your residence: ')
#
result = user_info(name, age, city)
print(result)

# HM#3.1.2

def max_number(a, b, c):
    num_list = [a,b,c]
    max_num = (max(num_list))
    return max_num

num_1 = int (input('Enter the first number: '))
num_2 = int (input('Enter the second number: '))
num_3 = int (input('Enter the third number: '))

result = max_number(num_1, num_2, num_3)
print('Max number is: {}'.format(result))

# HM#3.1.3

def max_line (* arg):
    max_len = max (arg, key = len)
    return max_len

line_1 = input('Enter the first line: ')
line_2 = input('Enter the second line: ')
line_3 = input('Enter the third line: ')

result = max_line(line_1, line_2, line_3)
print('The longest line is: : {}'.format(result))