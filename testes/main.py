for n in range(2, 10):
    for x in range(2, n): # no primeiro loop, n = 2, x = 2, então não existe indice no range(2, 2), ou seja, não entra no loop!!! Sempre que n for igual a x, não entra no loop.
        if n % x == 0:
            print(f"{n} igual a {x} * {n//x}")
            break