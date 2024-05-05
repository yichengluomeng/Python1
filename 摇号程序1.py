import random
import string

num = string.digits
STR = string.ascii_uppercase

number = "京"

Count = 1
while Count < 4:
    Car_Number = []
    print(f"当前为第{Count}次选择")
    for i in range(1, 21):
        for j in range(1, 7):
            if j == 1:
                number += random.choice(STR)
                number += " "
            else:
                number += random.choice(num + STR)
        Car_Number.append(number)
        number = "京"
    print(Car_Number)
    Key = input("请选择要选择的车牌").strip()
    if Key in Car_Number:
        exit(f"恭喜你选择成功,选择车牌为{Key}")
    else:
        print("不合法的选择")
    Count += 1
