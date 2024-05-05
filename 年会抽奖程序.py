"""
1.进入循环，三次抽奖While循环三次
2.生成员工ID
3.使用随机数产生中奖人员
4.将中奖人员存入列表，防止重复中奖
"""
import random

ID = []  # 定义员工编号
for i in range(1, 301):
    ID.append(i)  # 通过遍历的方式将员工号添加进列表中
# print(ID)
Count = 1  #
Reward = ["保温杯1个", "充电宝1个", "手机1个"]  # 奖励列表
while Count < 4:  # 几轮抽奖
    if Count == 1:  # 判断为第几次抽奖
        print(f"进入第{Count}次抽奖环节,本次奖励为{Reward[Count - 1]}")
    elif Count == 2:
        print(f"进入第{Count}次抽奖环节,本次奖励为{Reward[Count - 1]}")
    else:
        print(f"进入第{Count}次抽奖环节,本次奖励为{Reward[Count - 1]}")
    Key = int(input("请输入中奖人数"))  # 每轮抽奖人数不同，可进行手动输入
    a = random.sample(ID, Key)  # 随机获取中奖的人
    print(a)  # 打印中奖人数名单
    for i in a:  # 通过遍历的方式，将已中奖的人剔除
        ID.remove(i)  # 列表的移除指令
    Count += 1  # 防止进入死循环
