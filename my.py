def hiall(*names):
    for name in names:
        print('hello ' + name)


def cal(num1, num2, ope):
    if ope == '+':
        print(num1 + num2)
    elif ope == '-':
        print(num1 - num2)
    elif ope == '*':
        print(num1 * num2)
    else:
        if num2 == 0: num2 = 1
        print(num1 / num2)
print('hello1')
print('hello2')
print('hello3')
for x in range(1,6):
    print(x)
