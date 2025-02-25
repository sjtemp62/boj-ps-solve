# 문자열 3개 입력 후, 다음 문자열 찾기
num1 = input()
num2 = input()
num3 = input()

if num1.isdigit():
    num1 = int(num1)
    ans = num1 + 3
    if ans % 3 == 0 and ans % 5 == 0:
        print("FizzBuzz")
    elif ans % 3 == 0:
        print("Fizz")
    elif ans % 5 == 0:
        print("Buzz")
    else:
        print(ans)
elif num2.isdigit():
    num2 = int(num2)
    ans = num2 + 2
    if ans % 3 == 0 and ans % 5 == 0:
        print("FizzBuzz")
    elif ans % 3 == 0:
        print("Fizz")
    elif ans % 5 == 0:
        print("Buzz")
    else:
        print(ans)
elif num3.isdigit():
    num3 = int(num3)
    ans = num3 + 1
    if ans % 3 == 0 and ans % 5 == 0:
        print("FizzBuzz")
    elif ans % 3 == 0:
        print("Fizz")
    elif ans % 5 == 0:
        print("Buzz")
    else:
        print(ans)