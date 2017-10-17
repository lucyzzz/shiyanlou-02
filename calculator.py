#!/usr/bin/env python3
# coding : utf-8
import sys

# 应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
# 应纳税额 = 应纳税所得额 × 税率 － 速算扣除数


'''
养老保险：8%
医疗保险：2%
失业保险：0.5%
工伤保险：0%
生育保险：0%
公积金：6%
'''


def table(Taxable_Income):
    if 1500 >= Taxable_Income:
        return 0.03, 0
    elif 4500 >= Taxable_Income > 1500:
        return 0.1, 105
    elif 9000 >= Taxable_Income > 4500:
        return 0.2, 555
    elif 35000 >= Taxable_Income > 9000:
        return 0.25, 1005
    elif 55000 >= Taxable_Income > 35000:
        return 0.3, 2755
    elif 80000 >= Taxable_Income > 55000:
        return 0.35, 5505
    elif Taxable_Income > 80000:
        return 0.45, 13505


def tax(num,money):
    if money <= 0: #工资负数直接不计算
        print("Parameter Error")
        return
    insurance = money * 0.165                 #计算五险一金
    Taxable_Income = money - 3500 - insurance #应纳税额
    if Taxable_Income <= 0:  #如果应纳税所得额为负则不需要纳税.应纳税所得额=0
        Taxable_Income = 0.00
    tax_rate, take_out = table(Taxable_Income)  # 计算税率和速扣
    Tax_payable = Taxable_Income * tax_rate - take_out
    finally_money = money - Tax_payable - insurance
    print(num+":"+str('%.2f' % finally_money))  # 保留两位小数


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Parameter Error")

    for _ in range(1,len(sys.argv)):
        money = ''
        try:
            num = sys.argv[_].split(":")[0]
            money = int(sys.argv[_].split(":")[1])
        except ValueError:
            print("Parameter Error")
        except IndexError:
            print("Parameter Error")
            # print("you need input your wage like  ./calculator.py 5000")
        if money: tax(num,money)

