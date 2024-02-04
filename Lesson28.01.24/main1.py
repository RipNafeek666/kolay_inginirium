num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))
sign = input("Введите операцию(+ или - или / или *):")

if sign == "+":
    print(num1+num2)

elif sign == "-":
    print(num1-num2)
elif sign == "*":
    print(num1*num2)
elif sign == "/":
    if num2 != 0:
        print(num1/num2)
    else:
        print("На ноль делить нельзя")