def tax_calc(money):
    return money * 0.3

def pay_tax(tax):
    print("tax :", tax)

pay_tax(tax_calc(15000000000))