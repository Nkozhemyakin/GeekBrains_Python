# PEP 8
print ('Hello to HM#1#1')
Name = input ('Enter your name: ')
Lastname = input ('Enter your last name: ')
print ("Greetings " + Name +" "+ Lastname+"!")
print ("Well Done!")
print ("Let's calculate :)")
num = int(input ("Please enter any number: "))
print ("Your number plus 2 is: ")
print (2 + num)
age = int(input ('Please enter your age to continue: '))
if age >=18:
    print ("Access allowed")
    while True:
        num2 = int(input("Please enter number: "))
        if num2 == range (0,9):
            break

        if num2 > 10:
            print ("Wrong number!")
            continue
        break
    num2 = num2 * num2
    print (num2)
    print ("Good Job!")
    print ("Ok, and now, please enter two numbers: ")
    # не совсем уверен это ли имелось ввиду во втором задании :(
    a = int(input ("Please enter number A: "))
    b = int(input("Please enter number B: "))
    print ("Lets reverse your numbers!")
    print (b,a)
else:
    print ("Access denied")

