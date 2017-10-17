#!/usr/bin/env python3
# coding : utf-8
import sys

# 应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
# 应纳税额 = 应纳税所得额 × 税率 － 速算扣除数


def table(Taxable_Income):

    if  1500 >= Taxable_Income :
        return 0.03,0
    elif 4500 >= Taxable_Income > 1500:
        return 0.1,105
    elif 9000 >= Taxable_Income > 4500:
        return 0.2, 555
    elif 35000 >= Taxable_Income > 9500:
        return 0.25, 1005
    elif 55000 >= Taxable_Income > 35000:
        return 0.3, 2755
    elif 80000 >= Taxable_Income > 55000:
        return 0.35, 5505
    elif Taxable_Income > 80000 :
        return 0.45, 13505

def tax(money):
    if money < 3500:
        print(0.00)
        # print("扎心了,老哥你工资有点低不用交税")
        return
    Taxable_Income = money - 3500
    tax_rate,take_out = table(Taxable_Income)
    # print(Taxable_Income,tax_rate,take_out)
    Tax_payable = Taxable_Income*tax_rate-take_out
    print('%.2f'% Tax_payable) #保留两位小数

if __name__ == "__main__":
    money = ''
    try:
        money = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
    except IndexError:
        print("Parameter Error")
        # print("you need input your wage like  ./calculator.py 5000")
    if money:tax(money)