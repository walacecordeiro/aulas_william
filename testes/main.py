teste = list(range(2,10))
print(teste)

for n in teste:
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} é igual a {x} * {n//x}")
            break
    else:
        print(f"{n} é um número primo")