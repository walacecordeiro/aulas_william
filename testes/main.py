for n in range(2,10):
    for x in range(2,n): # Caso o range não seja iterável, a execução pula pro else
        if n % x == 0:
            print(f"{n} é igual a {x} * {n//x}")
            break
    else:
        print(f"{n} é um número primo")


import re

def verifica_padrao(texto):
    match texto:
        case texto if re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", texto):
            print("É um CPF válido.")
        case texto if re.fullmatch(r"\(\d{2}\) \d{4,5}-\d{4}", texto):
            print("É um número de celular válido.")
        case texto if re.fullmatch(r"\d{5}-\d{3}", texto):
            print("É um CEP válido.")
        case _:
            print("Padrão não reconhecido.")

verifica_padrao("123.456.789-09")           # CPF
verifica_padrao("(11) 98765-4321")          # Número de celular
verifica_padrao("01000-000")                # CEP
verifica_padrao("Olá, mundo!")              # Caso não reconhecido
