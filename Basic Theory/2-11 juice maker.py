def make_juice(fruit):
    return f"{fruit}+π₯€"

def add_ice(juice):
    return f"{juice}+π§"

def add_sugar(iced_juice):
    return f"{iced_juice}+π¬"

juice = make_juice("π")
cold_juice =add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

#f"{λ³μλͺ}" μ νλ©΄ μμμ μ€κ΄νΈ + λ³μλͺ λΆλΆμ λ³μ κ°μΌλ‘ λ°κΎΈμ΄ μ€λ€.(λ¬Έμμ΄μ λ³μ λ£λ λ°©λ²)
#returnμ ν¨μλ₯Ό λλΈλ€. κ·Έ λ€μ ν¨μ μ μ½λλ μ€νλμ§ μμ