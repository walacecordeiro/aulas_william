for n in range(2,10):
    for x in range(2,n): # Caso o range não seja iterável, a execução pula pro else
        if n % x == 0:
            print(f"{n} é igual a {x} * {n//x}")
            break
    else:
        print(f"{n} é um número primo")