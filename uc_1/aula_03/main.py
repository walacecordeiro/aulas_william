nome_do_usuario = "Walace Cordeiro dos Santos"
idade_do_usuario = 28
cidade_do_usuario = "Rio de Janeiro"

# formas de concatenar strings com variáveis em Python

# 1 - Concatenação simples com o operador , (vírgula) entre as variáveis e strings. ela acrescenta um espaço entre as variáveis e strings.
print("Olá, meu nome é",nome_do_usuario,"tenho",idade_do_usuario,"anos e moro no", cidade_do_usuario, ".")
# 2 - Concatenação com o operador + entre as variáveis e strings. Ela não acrescenta espaço entre as variáveis e strings.
print("Olá, meu nome é " + nome_do_usuario + " tenho " + str(idade_do_usuario) + " anos e moro no " + cidade_do_usuario + ".")
# 3 - Concatenação com f-string. Ela é a forma mais moderna e recomendada de concatenar strings com variáveis em Python. funciona da seguinte forma: f"texto {variável} texto"
print(f"Olá, meu nome é {nome_do_usuario}, tenho {idade_do_usuario} anos e moro no {cidade_do_usuario}.")