# GERADOR DE CPF V.1

from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero  # 9 números aleatórios
cont = 10
total = 0
for v in range(0, 9):
    mult = int(novo_cpf * cont)
    cont -= 1
    total += mult
formula = 11 - (total % 11)

if formula > 9:
    digito1 = 0
else:
    digito1 = formula


total2 = 0
cont2 = 11
for v in range(0, 10):
    mult2 = int(novo_cpf * cont2)
    cont2 -= 1
    total2 += mult2
formula2 = 11 - (total2 % 11)
if formula2 > 9:
    digito2 = 0
else:
    digito2 = formula2

novo_cpf = numero + str(digito1) + str(digito2)


print(novo_cpf)
print(len(novo_cpf))
